import pandas

# Fet item history and add after itemfeature


def read_csv():
    df = pandas.read_csv(
        './tianchi_mobile_recommend_train_user.csv')
    print 'ok'
    print 'yes'
    temp = df[df.behavior_type == 4].sort(
        columns='time', ascending=True)
    temp.to_csv(path_or_buf="all_buy_item_temp/" + str('all_buy_item'))


def filter_file(filename):
    f = open('all_buy_item_temp/' + filename)
    out = open('./' + filename, 'a')
    num = 0
    list_shop = []
    while 1:
        line = f.readline()
        if not line:
            break
        if num == 0:
            line = line.lstrip(',')
            out.write(line)
        else:
            a = line.split(',')
            string = ''
            for i in range(1, len(a)):
                string = string + ',' + a[i]
            list_shop.append(string)
        num += 1
    for record in list_shop:
        out.write(record.lstrip(','))
    out.close()
    f.close()


def getBuyHistory():
    f = open('itemfeature')
    out = open('item_all_feature', 'a')
    df = pandas.read_csv(
        './all_buy_item')
    group_item = df.groupby('item_id').size()
    dict_item = pandas.Series.to_dict(group_item)
    while 1:
        line = f.readline()
        if not line:
            break
        key = line.split(':')
        if dict_item.has_key(int(key[0])):
            out.write(
                key[0] + ":" + key[1].rstrip('\n') + ',' + str(dict_item[int(key[0])]) + '\n')
        else:
            out.write(key[0] + ":" + key[1].rstrip('\n') + ',' + '0' + '\n')
    f.close()
    out.close()


if __name__ == "__main__":
    read_csv()
    filter_file('all_buy_item')
    getBuyHistory()
