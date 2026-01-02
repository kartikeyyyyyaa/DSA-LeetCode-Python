def twosums():
    nums=list(map(int,input("enter array seperated by comma : ").split()))
    target=int(input( ))
    list2=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                list2.append(i)
                list2.append(j)
                print(list2)
                break
            else:
                continue
twosums()
