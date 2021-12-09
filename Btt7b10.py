import numpy as np
x = np.array([2, np.nan, 5, 9])
print("mean = ", np.nanmean(x))
print("median = ", np.nanmedian(x))

#kq:  mean =  5.333333333333333
#     median =  5.0
