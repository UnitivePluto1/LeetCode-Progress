class Solution:
    def reverse(self, x: int) -> int:
        
        rev = 0
        flag = 0
        if x < 0:
            flag = 1
            x = abs(x)
        while x>0:
            temp = x%10
            rev = rev*10 + temp
            x = x//10
        if rev<2**31 or -rev > 2**31 - 1:
            if flag == 1:
                return -rev
            return rev
        return 0
