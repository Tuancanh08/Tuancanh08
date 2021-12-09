import numpy as np

x = np.array([[14, 96],
              [np.nan, 82],
              [80, 67],
              [77, np.nan],
              [99, 87]])

print("X = ", x)

print("Giá trị lớn nhất: ", np.nanmax(x))
print("Giá trị bé nhất: ", np.nanmin(x))

# kq: X =  [[14. 96.]
#  [nan 82.]
#  [80. 67.]
#  [77. nan]
#  [99. 87.]]
# Giá trị lớn nhất:  99.0
# Giá trị bé nhất:  14.0
