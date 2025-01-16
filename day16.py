class Solution:
    def subarraySum(self, arr, target):
        # code here
        if sum(arr)<target: return [-1]
        start,end=0,0
        cs=0
        l,r=0,0
        while r<len(arr):
            if arr[r]==target: return [r+1,r+1]
            cs+=arr[r]
            if cs==target: return [l+1,r+1]
            while cs>target:
                cs-=arr[l]
                l+=1
                if cs==target:
                    return [l+1,r+1]
            r+=1
        return [-1]
