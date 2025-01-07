class Solution:
    def leaders(self, arr):
        # code here
        n = len(arr)
        if not n:
            return arr
        elif n == 1:
            return arr
        result = [arr[-1]]
        for i in range(n-2, -1, -1):
            if arr[i] >= result[-1]:
                result.append(arr[i]) 
        return result[::-1]
