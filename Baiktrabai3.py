print("Nhap so can tinh giai thua: ")
while True:
    n = int(input())
    if n<0:
        print("vui long nhap n > 0:")
    else:
        break

giaithua = 1;
for i in range(1,n+1):
    giaithua=giaithua * i;
print("Giai thừa của", n, "là",giaithua)
