class Solution(object):
    # def isPowerOfTwo(self, n):
    #     # if n<=0:
    #     #     return False
    #     # while n%2==0:
    #     #     n=n//2
    #     # if n==1:
    #     #     return True 
    #     # else :
    #     #     return False

    def isPowerOfTwo(self, n):
        if n<=0:
            return False
        if n==1:
            return True
        if n%2!=0:
            return False
        #recursive case
        return self.isPowerOfTwo(n//2)