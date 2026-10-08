class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        
        # Track the number of ways for the last two steps
        prev2 = 1  # Ways to reach step 1
        prev1 = 2  # Ways to reach step 2
        
        # Iteratively calculate ways for steps 3 to n
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return prev1