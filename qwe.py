b = []
i = int(input())
while i != 0:
    b.append(i)
z = len(b)
k = 0
for i in range(z):
    if b[i] < 0 and b[i+1]>0:
        k+=1
    elif b[i]>0 and b[b+1]<0:
        k+=1
print(k)




