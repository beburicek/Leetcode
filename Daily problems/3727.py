a=[1,2,3]
half_index=len(a)//2
for i in range(len(a)):
    a[i]=a[i]**2

a.sort()
print(sum(a[half_index:])-sum(a[:half_index]))

