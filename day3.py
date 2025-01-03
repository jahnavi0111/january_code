link -- https://www.geeksforgeeks.org/problems/peak-element/1?page=1&sortBy=submissions

class Solution:   
    def peakElement(self,arr, n):
        if(n==1):
            return 0
        elif(arr[0]>=arr[1]): 
            return 0
        elif(arr[-1]>=arr[-2]):
            return n-1
        else:
            j=1
            for j in range(len(arr)-1):
                if(arr[j]>=arr[j+1] and arr[j]>=arr[j-1]):
                    return j
        

