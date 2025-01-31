class Solution:
    def commonElements(self, arr1, arr2, arr3):
        #Code Here
        d1={}
        d2={}
        l=[]
        for i in arr2:
            if i not in d1.keys():
                d1[i]=1
        for i in arr3:
            if i not in d2.keys():
                d2[i]=1  
        for x in arr1:
            if d1.get(x) and d2.get(x):
                l.append(x)
                d1[x]=0
                d2[x]=0
        return l     
