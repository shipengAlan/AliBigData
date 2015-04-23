import pandas

# Group the train set by user_id, each file


def read_csv():
    f = open('user_list', 'a')
    df = pandas.read_csv(
        './train_user')
    num_of_user = df.groupby('user_id').size()
    print 'ok'
    list_of_user = num_of_user.index[num_of_user > 0]
    print 'yes'
    for user in list_of_user:
        print user
        f.write(str(user) + '\n')
        temp = df[df.user_id == user].sort(
            columns='time', ascending=True)
        temp.to_csv(path_or_buf="user_temp/" + str(user))
    f.close()


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
    f = open('user_temp/' + filename)
    out = open('user_data/' + filename, 'a')
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
    filenames = get_file_list('user_list')
    for filename in filenames:
        filter_file(filename)
        print filename + ' is ok'
    print 'all is ok'
