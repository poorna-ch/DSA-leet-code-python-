class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxcandies=max(candies)
        ans=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=maxcandies:
                ans.append(True)
            else:
                ans.append(False)
        return ans
            
                
    
