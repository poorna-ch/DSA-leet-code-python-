class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        for i in nums:
            arr=nums.sort()
            return nums[n/2]
