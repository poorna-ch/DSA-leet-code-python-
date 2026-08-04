class Solution(object):
    def isPalindrome(self, x):
        temp=x
        rev=0

        while temp>0:
            digit=temp%10
            temp//=10
            rev=(rev*10+digit)
        return rev==x 
