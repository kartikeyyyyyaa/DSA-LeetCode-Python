
def addTwoNumbers():
    l1=list(map(int,input("enter the element of the string").split()))
    l2=list(map(int,input("enter the element of the string").split()))
    l3=[]
    numl1="".join([str(n) for n in l1])
    numl2="".join([str(n) for n in l2])
    a=int(numl1)+int(numl2)
    while(a>0):
        b=a%10
        l3.append(b)
        a=a//10
    print(l3)
addTwoNumbers()