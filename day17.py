class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        a=arr
        m=max(arr)
        for i in a:
            if(i==m):
                arr.remove(m)
        print(arr)
        return max(arr)
    
