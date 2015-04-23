import time

# Get a child set of all data as a train set


def before_day(days, x, y):
    time_x = x.split(' ')[0]
    time_y = y.split(' ')[0]
    s_time = time.mktime(time.strptime(time_x, '%Y-%m-%d'))
    e_time = time.mktime(time.strptime(time_y, '%Y-%m-%d'))
    if s_time <= e_time + days * 24 * 60 * 60 and s_time > e_time:
        return True
    else:
        return False


def get5days_user():
    f = open('tianchi_mobile_recommend_train_user.csv')
    out = open('train_user', 'a')
    first_line = f.readline()
    out.write(first_line)
    print first_line
    while 1:
        line = f.readline()
        if not line:
            break
        line_item = line.rstrip('\n').split(',')
        print line_item[5]
        if before_day(5, line_item[5], "2014-12-12 00"):
            out.write(line)
    out.close()


if __name__ == '__main__':
    get5days_user()
