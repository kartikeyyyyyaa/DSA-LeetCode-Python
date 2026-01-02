import itertools
class Solution:
    def longestPalindrome(self, s: str) -> int:
        l1=[]
        l3=[]
        if len(s)==1:
            return 1
        if s==s[::-1]:
            print(len(s))
            return len(s)
            
        else:
         for i in range(len(s)):
            a=s[i]
            l1.append(a)
         for i in range(len(l1)):
          t1=list(itertools.permutations(l1,i))
          print(t1)
         l2=["".join(p) for p in t1]
         for i in range(len(l2)):
            b=l2[i]
            print(b)
            if b==b[::-1]:
                l3.append(b)
         print(l3)
         print(len(max(l3,key=len)))
Solution().longestPalindrome('bb')
