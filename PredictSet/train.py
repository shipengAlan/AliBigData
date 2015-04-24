#################################################
# logRegression: Logistic Regression
# Author : zouxy
# Date   : 2014-03-02
# HomePage : http://blog.csdn.net/zouxy09
# Email  : zouxy09@qq.com
# Change : shipeng.alan
#################################################
from numpy import *
import matplotlib.pyplot as plt
import time


# calculate the sigmoid function
def sigmoid(inX):
    return .5 * (1 + tanh(.5 * inX))
    # return 1.0 / (1 + exp(-inX))


# train a logistic regression model using some optional optimize algorithm
# input: train_x is a mat datatype, each row stands for one sample
#		 train_y is mat datatype too, each row is the corresponding label
#		 opts is optimize option include step and maximum number of iterations
def trainLogRegres(train_x, train_y, opts):
    # calculate training time
    startTime = time.time()

    numSamples, numFeatures = shape(train_x)
    alpha = opts['alpha']
    maxIter = opts['maxIter']
    weights = ones((numFeatures, 1))

    # optimize through gradient descent algorilthm
    for k in range(maxIter):
        # gradient descent algorilthm
        if opts['optimizeType'] == 'gradDescent':
            output = sigmoid(train_x * weights)
            error = train_y - output
            weights = weights + alpha * train_x.transpose() * error
        # stochastic gradient descent
        elif opts['optimizeType'] == 'stocGradDescent':
            for i in range(numSamples):
                output = sigmoid(train_x[i, :] * weights)
                error = train_y[i, 0] - output
                weights = weights + alpha * train_x[i, :].transpose() * error
        # smooth stochastic gradient descent
        elif opts['optimizeType'] == 'smoothStocGradDescent':
            # randomly select samples to optimize for reducing cycle
            # fluctuations
            dataIndex = range(numSamples)
            for i in range(numSamples):
                alpha = 4.0 / (1.0 + k + i) + 0.01
                randIndex = int(random.uniform(0, len(dataIndex)))
                output = sigmoid(train_x[randIndex, :] * weights)
                error = train_y[randIndex, 0] - output
                weights = weights + alpha * \
                    train_x[randIndex, :].transpose() * error
                # during one interation, delete the optimized sample
                del(dataIndex[randIndex])
        else:
            raise NameError('Not support optimize method type!')

    print 'Congratulations, training complete! Took %fs!' % (time.time() - startTime)
    return weights


# test your trained Logistic Regression model given test set
def testLogRegres(weights, test_x, test_y):
    numSamples, numFeatures = shape(test_x)
    matchCount = 0
    for i in xrange(numSamples):
        predict = sigmoid(test_x[i, :] * weights)[0, 0] > 0.5
        if predict == bool(test_y[i, 0]):
            matchCount += 1
    accuracy = float(matchCount) / numSamples
    return accuracy


def predict(weights, test_x, test_y, list_addr):
    numSamples, numFeatures = shape(test_x)
    Count = 0
    f = open('out', 'a')
    for i in xrange(numSamples):
        predict = sigmoid(test_x[i, :] * weights)[0, 0] > 0.5
        print predict
        if predict:
            f.write(list_addr[Count]+'\n')
        Count += 1
    f.close()

# show your trained logistic regression model only available with 2-D data


def showLogRegres(weights, train_x, train_y):
    # notice: train_x and train_y is mat datatype
    numSamples, numFeatures = shape(train_x)
    if numFeatures != 3:
        print "Sorry! I can not draw because the dimension of your data is not 2!"
        return 1

    # draw all samples
    for i in xrange(numSamples):
        if int(train_y[i, 0]) == 0:
            plt.plot(train_x[i, 1], train_x[i, 2], 'or')
        elif int(train_y[i, 0]) == 1:
            plt.plot(train_x[i, 1], train_x[i, 2], 'ob')

    # draw the classify line
    min_x = min(train_x[:, 1])[0, 0]
    max_x = max(train_x[:, 1])[0, 0]
    weights = weights.getA()  # convert mat to array
    y_min_x = float(-weights[0] - weights[1] * min_x) / weights[2]
    y_max_x = float(-weights[0] - weights[1] * max_x) / weights[2]
    plt.plot([min_x, max_x], [y_min_x, y_max_x], '-g')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()


def loadData():
    train_x = []
    train_y = []
    fileIn = open('train_data_set')
    for line in fileIn.readlines():
        lineArr = line.strip().split(',')
        train_x.append([1.0, float(lineArr[0]), float(lineArr[1]), float(lineArr[2]), float(lineArr[3]),
                        float(lineArr[4]), float(lineArr[5]), float(
                            lineArr[6]), float(lineArr[7]),
                        float(lineArr[8]), float(lineArr[9]), float(
                            lineArr[10]), float(lineArr[11]),
                        float(lineArr[12]), float(lineArr[13]), float(lineArr[14]), float(lineArr[15])])
        train_y.append(float(lineArr[16]))
    return mat(train_x), mat(train_y).transpose()


def loadPredectData():
    train_x = []
    train_y = []
    fileIn = open('predict_data_set')
    list_addr = []
    for line in fileIn.readlines():
        addr = line.rstrip('\n').rstrip(',').split(':')
        lineArr = addr[1].strip().split(',')
        train_x.append([1.0, float(lineArr[0]), float(lineArr[1]), float(lineArr[2]), float(lineArr[3]),
                        float(lineArr[4]), float(lineArr[5]), float(
                            lineArr[6]), float(lineArr[7]),
                        float(lineArr[8]), float(lineArr[9]), float(
                            lineArr[10]), float(lineArr[11]),
                        float(lineArr[12]), float(lineArr[13]), float(lineArr[14]), float(lineArr[15])])
        # train_y.append(float(lineArr[16]))
        list_addr.append(addr[0])
    return mat(train_x), mat(train_y).transpose(), list_addr


if __name__ == '__main__':
    """
    a = numpy.loadtxt("test.data", delimiter="	")
    table_x = numpy.array(a[:, 0:2])
    table_y = numpy.array(a[:, 2], dtype=numpy.int)
    """
    table_x, table_y = loadData()
    opts = {}
    opts['alpha'] = 0.01
    opts['maxIter'] = 500
    opts['optimizeType'] = 'smoothStocGradDescent'

    optimalWeights = trainLogRegres(
        train_x=table_x, train_y=table_y, opts=opts)
    accuracy = testLogRegres(optimalWeights, table_x, table_y)
    tx, ty, addr = loadPredectData()
    predict(optimalWeights, tx, ty, addr)
    # show the result
    print "show the result..."
    print 'The classify accuracy is: %.3f%%' % (accuracy * 100)
    #showLogRegres(optimalWeights, table_x, table_y)
