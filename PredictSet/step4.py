import pandas
import time

# Get Item feature except history buy log


def read_csv():
    f = open('item_list', 'a')
    df = pandas.read_csv(
        './predict_user')
    num_of_item = df.groupby('item_id').size()
    print 'ok'
    list_of_item = num_of_item.index[num_of_item > 0]
    print 'yes'
    for i in list_of_item:
        print i
        f.write(str(i) + '\n')
        temp = df[df.item_id == i].sort(
            columns='time', ascending=True)
        temp.to_csv(path_or_buf="item_temp/" + str(i))
        string = getItemData(str(i))
        ff = open('itemfeature', 'a')
        ff.write(str(i) + ":" + string + "\n")
        ff.close()
    f.close()


def getDay(x, y):
    time_x = x.rstrip('\n')
    time_y = y.rstrip('\n')
    s_time = time.mktime(time.strptime(time_x, '%Y-%m-%d %H'))
    e_time = time.mktime(time.strptime(time_y, '%Y-%m-%d %H'))
    return str((e_time - s_time) / 3600)


def getItemData(filename):
    ff = open("item_temp/" + filename)
    first_line = ff.readline()
    click = []
    buy = []
    save = []
    shop = []
    buy_time = "2014-12-14 00"
    while 1:
        line = ff.readline()
        if not line:
            break
        line_item = line.split(',')
        if int(line_item[3]) == 1:
            click.append(line_item[1])
        elif int(line_item[3]) == 2:
            save.append(line_item[1])
        elif int(line_item[3]) == 3:
            shop.append(line_item[1])
        elif int(line_item[3]) == 4:
            buy.append(line_item[1])
            buy_time = line_item[6]
    string = str(len(click)) + ',' + str(len(save)) + ',' + str(len(shop)
                                                                ) + ',' + str(len(buy)) + ',' + getDay(buy_time, "2014-12-19 00")
    ff.close()
    return string


def get_file_list(filename):
    f = open(filename)
    a = []
    while 1:
        line = f.readline()
        if not line:
            break
        a.append(line.rstrip('\n'))
    return a


def filter_file(filename):
    f = open('item_temp/' + filename)
    out = open('item_data/' + filename, 'a')
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
if __name__ == "__main__":
    read_csv()
    filenames = get_file_list('item_list')
    for filename in filenames:
        filter_file(filename)
        print filename + ' is ok'
    print 'all is ok'
