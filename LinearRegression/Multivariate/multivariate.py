"""
high level support for doing this and that.
"""
from numpy import loadtxt, zeros, mean, std

#Evaluate the linear regression
def feature_normalize(X):
    '''
    Returns a normalized version of X where
    the mean value of each feature is 0 and the standard deviation
    is 1. This is often a good preprocessing step to do when
    working with learning algorithms.
    '''
    mean_r = []
    std_r = []

    X_norm = X
    n_c = X.shape[1]
    for i in range(n_c):
        m = mean(X[:, i])
        s = std(X[:, i])
        mean_r.append(m)
        std_r.append(s)
        X_norm[:, i] = ((X_norm[:, i] - m) / s)
    return X_norm, mean_r, std_r

# Load the data set
data = loadtxt('ex1data2.txt', delimiter=',')

X = data[:, :2]
Y = data[:, 2]

# Total size of Training set
m = Y.size

# Scale features to make them zero mean
X = feature_normalize(X)

# Initial theta 
theta = zeros(shape=(2, 1))


