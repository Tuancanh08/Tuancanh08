import numpy as np
arr = np.array([[7, 4, 2], [3, 9, 5]])
print("median arr (axis = 0) = ", np.median(arr, axis=0))
print("median arr (axis = 1) = ", np.median(arr, axis=1))

 #kq: median arr (axis = 0) =  [5.  6.5 3.5]
 #    median arr (axis = 1) =  [4. 5.]
