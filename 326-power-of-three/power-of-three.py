class Solution(object):
    # def isPowerOfThree(self, n):
    #     if n<=0:
    #       return False
    #     while n%3==0:
    #         n=n//3
    #     if n==1:
    #         return True
    #     else:
    #         return False
    def isPowerOfThree(self, n):
        if n<=0:
            return False
        if n==3 or n==1:
            return True
        if n%3!=0:
            return False
         #recursive case
        return self.isPowerOfThree(n//3)
