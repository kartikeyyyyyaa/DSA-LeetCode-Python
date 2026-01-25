def twosums():
    nums=list(map(int,input("enter array seperated by comma : ").split()))
    target=int(input( ))
    list3=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                list3.append(i)
                list3.append(j)
                print(list3)
                break
            else:
                continue
twosums()

