lst = [3, 54, 6, 7, 8, 9]
lenth = len(lst)

for i in range(0, lenth - 1):
	for j in range(i + 1, lenth):
		if(lst[i]>lst[j]):
			temp = lst[i]
			lst[i]=lst[j]
			lst[j]=temp
print(lst)
