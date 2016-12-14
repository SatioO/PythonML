# '''
# LOGISTIC REGRESSION
# '''

# from numpy import loadtxt, where, ones, zeros, e, log
# from pylab import scatter, show, xlabel, ylabel, legend

# def sigmoid(h):
#     '''
#     Comput sigmoid for logistic regression
#     '''
#     g = 1.0 / (1.0 + e ** (-1.0 * h))
#     return g

# def compute_cost(X, Y, theta):
#     '''
#     Comput cost for logistic regression
#     '''
#     theta.shape = (1, 3)

#     m = Y.size

#     h = sigmoid(X.dot(theta.T))
#     J = (1.0 / m) * ((-Y.T.dot(log(h))) - ((1.0 - Y.T).dot(log(1.0 - h)))).sum()
#     grad = 1.0 * m * (X.T.dot(h - Y))
#     return [J, grad]

# # Load Training set into program
# data = loadtxt('ex2data1.txt', delimiter=',')

# # Assign data to input and output variables
# X = data[:, 0:2]
# Y = data[:, 2]

# #  Isolate positive and results
# pos = where(Y == 1)
# neg = where(Y == 0)

# # Visualize the Training-set
# scatter(X[pos, 0], X[pos, 1], marker='+', c='b')
# scatter(X[neg, 0], X[neg, 1], marker='o', c='r')
# xlabel('Exam 1 score')
# ylabel('Exam 2 score')
# legend(['Not Admitted', 'Admitted'])
# show()

# # Append X by 1 row vector
# m, n = X.shape
# Y.shape = (m, 1)
# it= ones(shape=(m, 3))
# it[:, 1:3] = X

# # Initialize theta
# theta = zeros(shape=(n + 1,1))

# # compute function 

# J, grad = compute_cost(it, Y, theta)

class Log_R:
    def __init__(self):
        __secretcount = 0
    
logistic =  Log_R()
print logistic.__secretcount