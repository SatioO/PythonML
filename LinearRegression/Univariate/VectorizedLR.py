'''
VECTORIZED IMPLEMENTATION
'''
from numpy import loadtxt, zeros, ones, transpose
from pylab import scatter, show, plot

def compute_cost(X, Y, theta):
    # Number of training samples
    m = Y.size

    predictions = X.dot(theta).flatten()
    sqErrors = (predictions - Y) ** 2

    J = (1.0 / (2 * m)) * sqErrors.sum()

    return J

def gradientDescent(X, Y, theta, alpha, iterations):

    m = Y.size

    for i in range(iterations):
        predictions = (X.dot(theta).flatten()) - Y
        delta = 1.0 / m * (predictions.transpose().dot(X)).transpose()
        theta = theta.flatten() - (alpha * delta)
    return theta

# Load Training Set into example
data = loadtxt('ex1data1.txt', delimiter=',')

# Isolate Training Set into input and output variables
X = data[:, 0]
Y = data[:, 1]

# Set theta size
theta = zeros(shape=(2, 1))

# set the training set size
m = Y.size

#  As X subscript 0 = 1, append it to 
it = ones(shape=(m, 2))
it[:, 0] = X

print(compute_cost(it, Y, theta))

# Set Number of iterations to perform
iterations = 5000

# Set alpha value
alpha = 0.01

theta = gradientDescent(it, Y, theta, alpha, iterations)

scatter(X, Y, s=20,c='none')
result = it.dot(theta)
plot(data[:, 0], result)
show()