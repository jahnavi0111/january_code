def findDuplicates(self, arr):
        hashmap={}
        for i in arr:
            hashmap[i]=1 if i not in hashmap else hashmap[i]+1
        res=[]
        for i in hashmap:
            if hashmap[i]>1:
                res.append(i)
        return res
