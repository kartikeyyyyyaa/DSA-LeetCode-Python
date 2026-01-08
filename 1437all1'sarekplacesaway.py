class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        b=[]
        for i in range(len(nums)):
            if nums[i]==1:
                print(i)
                b.append(i)
        i=0
        j=1
        while j<len(b):
            if (abs(b[i]-b[j])-1)>=k:
                print(abs(b[i]-b[j])-1)
                i+=1
                j+=1
                pass
            else:
                return False
                break
        return True
        