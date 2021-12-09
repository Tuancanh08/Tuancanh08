import numpy as np

X = np.array([[1, 2], [3, 4]])
print("Mean X = ", np.mean(X))
print("Mean X với axis = 0: ", np.mean(X, axis=0))
print("Mean X với axis = 1: ", np.mean(X, axis=1))

#kq: Mean X =  2.5
#    Mean X với axis = 0:  [2. 3.]
#    Mean X với axis = 1:  [1.5 3.5]
