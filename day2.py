link to question :
https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&sortBy=submissions

class Solution:
    def missingNumber(self, arr):
        sum=0
        if(1 not in arr):
            return 1
        
        elif(len(arr)==1):
            return arr[0]+1
            
        else:
            for i in arr:
                sum+=i
                
            return int(((((len(arr)+1)*(len(arr)+2))/2)-sum))
                
