class Solution:
    def sorts(self,a):
            a=list(a)
            a.sort()
            return "".join(a)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        for i in strs:
            b=self.sorts(i)
            if b in dict1:
                dict1[b].append(i)
            else:
                dict1[b]=[i]
        return list(dict1.values())

