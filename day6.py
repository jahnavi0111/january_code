class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        maxi = arr[0]
        ndmaxi =-1
        n = len(arr)
        
        for i in range(0,n):
            if arr[i]>maxi:
                ndmaxi =maxi
                maxi = arr[i]
            elif arr[i]<maxi and arr[i]>ndmaxi:
                ndmaxi = arr[i]
        return ndmaxi
