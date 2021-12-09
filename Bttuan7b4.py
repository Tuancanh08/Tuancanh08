import numpy as np

a = np.zeros((2, 512*512), dtype=np.float32)
a[0, :] = 1.0
a[1, :] = 0.1
print("mean a = ", np.mean(a, dtype=np.float64))

#kq: mean a =  0.5500000007450581
