A = [1,1,2,6,8,9,4,5,6,45,34,66,44,37,78]
B = []
print("Các số nhỏ hơn 30 là: ")
for x in A:
	if x < 30:
		print(x)
		B.append(x)
print(B)
n = input("nhập n:")
n = int(n)
print("Các số lớn hơn n là:")
for x in A:
	if x > n:
		print(x)
