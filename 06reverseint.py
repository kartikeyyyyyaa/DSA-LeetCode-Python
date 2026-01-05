a=int(input("Enter the Number: "))
l=[]
if a<0:
    b=-a
else:
    b=a
while b>0:
    c=b%10
    b=b//10
    l.append(c)
print(l)
num="".join([str(n) for n in l])
num1=int(num)
if a<0:
    print(-num1)
else:
    print(num1)
