import pandas
import time


# collect the user-item data


def getPreditcItem():
    df = pandas.read_csv('tianchi_mobile_recommend_train_item.csv')
    ll = pandas.Series.tolist(df['item_id'])
    return ll


def getItemFeature():
    f = open('item_all_feature')
    dict_item_feature = {}
    while 1:
        line = f.readline()
        if not line:
            break
        line_item = line.split(':')
        dict_item_feature[line_item[0]] = line_item[1].rstrip('\n')
    list_predict_item = getPreditcItem()
    dict_predict_item_feature = {}
    c = 0
    h = 0
    for i in list_predict_item:
        if dict_item_feature.has_key(str(i)):
            h += 1
            dict_predict_item_feature[str(i)] = dict_item_feature[str(i)]
        else:
            c += 1
            #dict_predict_item_feature[str(i)] = "0,0,0,0,120.0,0"
    # print h, c
    print len(dict_predict_item_feature)
    # print len(list_predict_item)
    return dict_predict_item_feature


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


def day2history_user_item():
    f = open('predict_user')
    dict_user_item_feature = {}
    first_line = f.readline()
    while 1:
        line = f.readline()
        if not line:
            break
        list_item = line.split(',')
        if before_days(2, list_item[5].rstrip('\n'), "2014-12-16 00"):
            if dict_user_item_feature.has_key(list_item[0] + "," + list_item[1]):
                if int(list_item[2]) == 1:
                    dict_user_item_feature[
                        list_item[0] + "," + list_item[1]][0] += 1
                    click_time = getDay(
                        list_item[5].rstrip('\n'), "2014-12-19 00")
                    if dict_user_item_feature[list_item[0] + "," + list_item[1]][3] > click_time:
                        dict_user_item_feature[
                            list_item[0] + "," + list_item[1]][3] = click_time
                if int(list_item[2]) == 2:
                    dict_user_item_feature[
                        list_item[0] + "," + list_item[1]][1] += 1
                    save_time = getDay(
                        list_item[5].rstrip('\n'), "2014-12-19 00")
                    if dict_user_item_feature[list_item[0] + "," + list_item[1]][4] > save_time:
                        dict_user_item_feature[
                            list_item[0] + "," + list_item[1]][4] = save_time
                if int(list_item[2]) == 3:
                    dict_user_item_feature[
                        list_item[0] + "," + list_item[1]][2] += 1
                    shop_time = getDay(
                        list_item[5].rstrip('\n'), "2014-12-19 00")
                    if dict_user_item_feature[list_item[0] + "," + list_item[1]][5] > shop_time:
                        dict_user_item_feature[
                            list_item[0] + "," + list_item[1]][5] = shop_time
            else:
                dict_user_item_feature[
                    list_item[0] + "," + list_item[1]] = [0, 0, 0, 72, 72, 72]
                if int(list_item[2]) == 1:
                    dict_user_item_feature[
                        list_item[0] + "," + list_item[1]][0] += 1
                    click_time = getDay(
                        list_item[5].rstrip('\n'), "2014-12-19 00")
                    if dict_user_item_feature[list_item[0] + "," + list_item[1]][3] > click_time:
                        dict_user_item_feature[
                            list_item[0] + "," + list_item[1]][3] = click_time
                if int(list_item[2]) == 2:
                    dict_user_item_feature[
                        list_item[0] + "," + list_item[1]][1] += 1
                    save_time = getDay(
                        list_item[5].rstrip('\n'), "2014-12-19 00")
                    if dict_user_item_feature[list_item[0] + "," + list_item[1]][4] > save_time:
                        dict_user_item_feature[
                            list_item[0] + "," + list_item[1]][4] = save_time
                if int(list_item[2]) == 3:
                    dict_user_item_feature[
                        list_item[0] + "," + list_item[1]][2] += 1
                    shop_time = getDay(
                        list_item[5].rstrip('\n'), "2014-12-19 00")
                    if dict_user_item_feature[list_item[0] + "," + list_item[1]][5] > shop_time:
                        dict_user_item_feature[
                            list_item[0] + "," + list_item[1]][5] = shop_time

    return dict_user_item_feature


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
    dict_predict_item_feature = getItemFeature()
    dict_user_item_feature = day2history_user_item()
    dict_user_feature = getUserFeature()
    out = open('predict_data_set', 'a')
    for k, v in dict_predict_item_feature.items():
        for kk, vv in dict_user_feature.items():
            '''
            if not dict_user_item_feature.has_key(str(kk) + "," + str(k)):
                # print str(kk) + ',' + str(k), "is not ok"
                item_id = str(k)
                user_id = str(kk)
                string = "0,0,0,72,72,72," + \
                    dict_predict_item_feature[item_id] + ','
                string = string + dict_user_feature[user_id]
                #out.write(str(kk) + "," + str(k)+":"+string + '\n')
            '''
            if dict_user_item_feature.has_key(str(kk) + "," + str(k)):
                list_item = dict_user_item_feature[str(kk) + "," + str(k)]
                string = ''
                for i in list_item:
                    string = string + str(i) + ","
                item_id = str(k)
                user_id = str(kk)
                string = string + dict_predict_item_feature[item_id] + ','
                string = string + dict_user_feature[user_id]
                print string
                out.write(str(kk) + "," + str(k) + ":" + string + '\n')
    out.close()
