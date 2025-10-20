class Solution:
    def isUgly(self, n: int) -> bool:
        def check(n):
            if n == 1:
                return True
            if n%2 == 0:
                return check(n/2)
            elif n%3 == 0:
                return check(n/3)
            elif n%5 ==0:
                return check(n/5)
            else:
                return False
        if n <= 0:
            return False
        return check(n)
        
            