class solution: 
    def convert():
        numrows=int(input("enter the number of rows: "))
        s=input()
        if numrows==1: 
            return s
        res=""
        for r in range(numrows):
            increment=2*(numrows-1)
            for i in range(r,len(s),increment):
                res+=s[i]
                if(r>0 and r<numrows-1 and i+increment-2*r<len(s)):
                    res+=s[i+increment-2*r]
        print(res)
        return res
solution.convert()

