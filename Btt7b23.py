import numpy as np
coins = np.random.choice([0, 1], size=1000, p=[0.2, 0.8]) # random.choice sẽ lấy ngẫu nhiên các phần tử trong mảng ở tham số đầu tiên với xác suất ở tham số p
print("% số lần tung được mặt ngửa: ", (coins == 0).mean() * 100)
print("% số lần tung được mặt úp: ", (coins == 1).mean() * 100)

#kq: % số lần tung được mặt ngửa:  17.7
# % số lần tung được mặt úp:  82.3
