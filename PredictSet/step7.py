import pandas
import time
# get item statistics data


def get_file_list(filename):
    f = open(filename)
    a = []
    while 1:
        line = f.readline()
        if not line:
            break
        a.append(line.rstrip('\n'))
    return a


def getDay(x, y):
    time_x = x.rstrip('\n')
    time_y = y.rstrip('\n')
    s_time = time.mktime(time.strptime(time_x, '%Y-%m-%d %H'))
    e_time = time.mktime(time.strptime(time_y, '%Y-%m-%d %H'))
    return str((e_time - s_time)/3600)

if __name__ == '__main__':
    filenames = get_file_list('item_list')
    f = open('itemfeature', 'a')
    for filename in filenames:
        ff = open("item_temp/" + filename)
        first_line = ff.readline()
        click = []
        buy = []
        save = []
        shop = []
        buy_time = "2014-12-13 00"
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
                                                                    ) + ',' + str(len(buy)) + ',' + getDay(buy_time, "2014-12-18 00")
        ff.close()
        f.write(filename + ':' + string + '\n')
        print filename + ':' + string
        print filename, 'is ok'
    f.close()
    print 'all is ok'
