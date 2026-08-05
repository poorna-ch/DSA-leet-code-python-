# class Solution(object):
#     def tribonacci(self, n):
#         if n==0 :
#             return n
#         if n<=2:
#             return 1
#         return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3) 
    # o(n^3)
    # so , convert into o(n) by storing values into memory
class Solution(object):
    def tribonacci(self, n):

        if not hasattr(self, "memo"):
            self.memo = {}

        if n in self.memo:
            return self.memo[n]

        if n == 0:
            return 0

        if n <= 2:
            return 1

        self.memo[n] = (
            self.tribonacci(n-1)
            + self.tribonacci(n-2)
            + self.tribonacci(n-3)
        )

        return self.memo[n]
        