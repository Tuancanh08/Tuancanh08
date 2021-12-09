import numpy as np

x = np.array([[14, 96],
              [46, 82],
              [80, 67],
              [77, 91],
              [99, 87]])

print("X = ", x)

print("Giá trị lớn nhất: ", np.amax(x))
print("Giá trị bé nhất: ", np.amin(x))

print("Giá trị lớn nhất (axis = 0): ", np.amax(x, axis=0))
print("Giá trị lớn nhất (axis = 1): ", np.amax(x, axis=1))

# kq: X =  [[14 96]
#  [46 82]
#  [80 67]
#  [77 91]
#  [99 87]]
# Giá trị lớn nhất:  99
# Giá trị bé nhất:  14
# Giá trị lớn nhất (axis = 0):  [99 96]
# Giá trị lớn nhất (axis = 1):  [96 82 80 91 99]
