    def reverseInGroups(self, arr, k):
        n=len(arr)
        for i in range(0,n,k):
            left,right=i,min(i+k-1,n-1)
            while left<right:
                arr[left],arr[right]=arr[right],arr[left]
                left+=1
                right-=1
