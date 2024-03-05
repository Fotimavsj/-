import random
n= int(input("n="))
m=[]
for i in range(0,n):
    a=random.randint(0,n)
    m.append(a)
print(m)
s=0
for i in m:
    s=s+i
print(s/n)