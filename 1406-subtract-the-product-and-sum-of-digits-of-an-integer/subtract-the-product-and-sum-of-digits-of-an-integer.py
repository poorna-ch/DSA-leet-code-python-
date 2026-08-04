class Solution(object):
    def subtractProductAndSum(self, n):
        temp=n
        sum_digit=0
        pro_digit=1
        while temp>0:
            digit=temp%10
            temp//=10
            sum_digit+=digit
            pro_digit*=digit
        return pro_digit-sum_digit
         
         