class Solution(object):
    def majorityElement(self, nums):
        count={}
        res,max_count=0,0
        for n in nums:
            count[n]=count.get(n,0)+1
            if count[n]>max_count:
                res=n
            else:
                res
            max_count=max(count[n],max_count)
        return res
        