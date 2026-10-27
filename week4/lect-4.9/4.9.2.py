# create the below matrix A and B with python

import numpy

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,2,1],[6,2,3],[4,2,1]]

X = numpy.mat(A)
Y = numpy.mat(B)

print(X * Y)
