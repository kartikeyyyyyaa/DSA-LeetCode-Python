class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i=0
        j=len(nums)-1
        k=0
        while k<=j:
          if nums[k]==1:
            k+=1
          elif nums[k]==0:
            a=nums[k]
            nums[k]=nums[i]
            nums[i]=a
            i+=1
            k+=1
          else:
            nums[j],nums[k]=nums[k],nums[j]
            j-=1
        return nums
        
