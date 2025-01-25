  def maximumMeetings(self,start,end):
        # code here
        ans=0
        arr=[(abs(start[i]-end[i]),start[i],end[i]) for i in range(len(start))]
        arr.sort(key=lambda x:x[0])
        dp=[-1]*(max(end)+1)
        for x,y,z in arr:
            #print(dp[y:z+1])
            if 1 not in dp[y:z+1]:
                for j in range(y,z+1):
                    dp[j]=1
                #print(y,z)
                ans=ans+1
        
        return ans
