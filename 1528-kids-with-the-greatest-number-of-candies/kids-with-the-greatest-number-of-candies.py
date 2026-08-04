class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        return[(i+extraCandies)>=max(candies) for i in candies] 
        # list comphrension
        #   --------or--------
        # maxcandies=max(candies)
        # ans=[]
        # for i in range(len(candies)):
        #     if candies[i]+extraCandies>=maxcandies:
        #         ans.append(True)
        #     else:
        #         ans.append(False)
        # return ans
            
                
    
