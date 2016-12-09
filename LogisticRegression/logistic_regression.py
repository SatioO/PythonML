'''
LOGISTIC REGRESSION
'''

from numpy import loadtxt, where
from pylab import scatter, show, xlabel, ylabel, legend

# Load Training set into program
data = loadtxt('ex2data1.txt', delimiter=',')

# Assign data to input and output variables
X = data[:, 0:2]
Y = data[:, 2]

#  Isolate positive and results
pos = where(Y == 1)
neg = where(Y == 0)

# Visualize the Training-set
scatter(X[pos, 0], X[pos, 1], marker='+', c='b')
scatter(X[neg, 0], X[neg, 1], marker='o', c='r')
xlabel('Exam 1 score')
ylabel('Exam 2 score')
legend(['Not Admitted', 'Admitted'])
show()

# Append X by 1 row vector
m, n = X.shape


