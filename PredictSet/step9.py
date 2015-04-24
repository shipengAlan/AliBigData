import time

# Get user-item last 3days history info and label


def getTestUserItem():
    f = open('test_user')
    first_line = f.readline()
    dict_user_item = {}
    while 1:
        line = f.readline()
        if not line:
            break
        list_item = line.split(',')
        if not dict_user_item.has_key(list_item[0] + "," + list_item[1] + "," + list_item[4]):
            dict_user_item[
                list_item[0] + "," + list_item[1] + "," + list_item[4]] = 0
        if 4 == int(list_item[2]):
            dict_user_item[
                list_item[0] + "," + list_item[1] + "," + list_item[4]] = 1
    f.close()
    c = 0
    d = 0
    for k, v in dict_user_item.items():
        # print k, v
        if v == 1:
            c += 1
        else:
            d += 1
    print d, c
    return dict_user_item


def before_days(days, x, y):
    time_x = x.split(' ')[0]
    time_y = y.split(' ')[0]
    s_time = time.mktime(time.strptime(time_x, '%Y-%m-%d'))
    e_time = time.mktime(time.strptime(time_y, '%Y-%m-%d'))
    if s_time >= e_time:
        return True
    else:
        return False


def getDay(x, y):
    time_x = x.rstrip('\n')
    time_y = y.rstrip('\n')
    s_time = time.mktime(time.strptime(time_x, '%Y-%m-%d %H'))
    e_time = time.mktime(time.strptime(time_y, '%Y-%m-%d %H'))
    return int((e_time - s_time) / 3600)


def day2history_user_item(dict_user_item_label):
    f = open('train_user')
    dict_user_item_feature = {}
    dict_user_item_time = {}
    first_line = f.readline()
    while 1:
        line = f.readline()
        if not line:
            break
        list_item = line.split(',')
        if before_days(2, list_item[5].rstrip('\n'), "2014-12-15 00"):
            if dict_user_item_feature.has_key(list_item[0] + "," + list_item[1] + "," + list_item[4]):
                if int(list_item[2]) == 1:
                    dict_user_item_feature[
                        list_item[0] + "," + list_item[1] + "," + list_item[4]][0] += 1
                    click_time = getDay(
                        list_item[5].rstrip('\n'), "2014-12-18 00")
                    # print click_time,(dict_user_item_feature[list_item[0] +
                    # "," + list_item[1] + "," +
                    # list_item[4]][3]),type(click_time),type((dict_user_item_feature[list_item[0]
                    # + "," + list_item[1] + "," + list_item[4]][3]))
                    if dict_user_item_feature[list_item[0] + "," + list_item[1] + "," + list_item[4]][3] > click_time:
                        dict_user_item_feature[
                            list_item[0] + "," + list_item[1] + "," + list_item[4]][3] = click_time
                if int(list_item[2]) == 2:
                    dict_user_item_feature[
                        list_item[0] + "," + list_item[1] + "," + list_item[4]][1] += 1
                    save_time = getDay(
                        list_item[5].rstrip('\n'), "2014-12-18 00")
                    if dict_user_item_feature[list_item[0] + "," + list_item[1] + "," + list_item[4]][4] > save_time:
                        dict_user_item_feature[
                            list_item[0] + "," + list_item[1] + "," + list_item[4]][4] = save_time
                if int(list_item[2]) == 3:
                    dict_user_item_feature[
                        list_item[0] + "," + list_item[1] + "," + list_item[4]][2] += 1
                    shop_time = getDay(
                        list_item[5].rstrip('\n'), "2014-12-18 00")
                    if dict_user_item_feature[list_item[0] + "," + list_item[1] + "," + list_item[4]][5] > shop_time:
                        dict_user_item_feature[
                            list_item[0] + "," + list_item[1] + "," + list_item[4]][5] = shop_time
            else:
                dict_user_item_feature[
                    list_item[0] + "," + list_item[1] + "," + list_item[4]] = [0, 0, 0, 72, 72, 72]
    return dict_user_item_feature


def getItemFeature():
    f = open('item_all_feature')
    dict_item_feature = {}
    while 1:
        line = f.readline()
        if not line:
            break
        line_item = line.split(':')
        dict_item_feature[line_item[0]] = line_item[1].rstrip('\n')
    return dict_item_feature


def getUserFeature():
    f = open('userfeature')
    dict_user_feature = {}
    while 1:
        line = f.readline()
        if not line:
            break
        line_item = line.split(':')
        dict_user_feature[line_item[0]] = line_item[1].rstrip('\n')
    return dict_user_feature


if __name__ == "__main__":
    dict_user_item = getTestUserItem()
    dict_user_item_feature = day2history_user_item(
        dict_user_item)
    dict_item_feature = getItemFeature()
    dict_user_feature = getUserFeature()
    out = open('train_data_set', 'a')
    for k, v in dict_user_item.items():
        if not dict_user_item_feature.has_key(k):
            continue
        list_item = dict_user_item_feature[k]
        string = ''
        for i in list_item:
            string = string + str(i) + ","
        k_item = k.split(',')
        item_id = k_item[1]
        user_id = k_item[0]
        string = string + dict_item_feature[item_id] + ','
        string = string + dict_user_feature[user_id]
        string = string + str(v)
        print string
        out.write(string+'\n')
    out.close()
