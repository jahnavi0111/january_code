link --> https://www.geeksforgeeks.org/problems/maximum-nesting-depth-of-the-parentheses/1?page=1&category=Arrays,Strings&sortBy=accuracy


def maxDepth(self, s):
        # Code here
        if s=="":
            return 0
        st=[]
        maxi=-1
        for i in s:
            if i == ")":
                if st and st[-1]=="(":
                    maxi = max(maxi,len(st)) 
                    st.pop()
            elif i=="(":  
                st.append(i)
        return maxi
