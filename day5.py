link --> https://leetcode.com/problems/minimum-index-sum-of-two-lists/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        maxi=0
        index=0
        p=[]
        for i,v1 in enumerate(list1):
            for j,v2 in enumerate(list2):
                if(v1==v2 and p==[]):
                    index=i+j
                    p.append(v1)
                elif(v1==v2 and p!=[] and index>=(i+j)):
                    index=i+j
                    p.append(v1)
        return p
