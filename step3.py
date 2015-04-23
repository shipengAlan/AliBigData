import pandas

# Get user feature


def get_file_list(filename):
    f = open(filename)
    a = []
    while 1:
        line = f.readline()
        if not line:
            break
        a.append(line.rstrip('\n'))
    return a


if __name__ == '__main__':
    filenames = get_file_list('user_list')
    f = open('userfeature', 'a')
    for filename in filenames:
        print filename, 'is ok'
        df = pandas.read_csv('user_data/' + filename)
        num_of_behavior = df.groupby('behavior_type').size()
        string = ''
        dd = pandas.Series.to_dict(num_of_behavior)
        for i in range(1, 5):
            if dd.has_key(i):
                string = string + str(num_of_behavior[i]) + ","
            else:
                string = string + '0' + ','
        f.write(filename + ':' + string + '\n')
    f.close()
    print 'all is ok'
