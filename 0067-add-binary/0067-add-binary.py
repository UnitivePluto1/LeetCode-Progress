class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        carry = 0
        sum = ""

        a,b = a[::-1], b[::-1]
        for i in range(max(len(a),len(b))):
            A = int(a[i]) if i < len(a) else 0
            B = int(b[i]) if i < len(b) else 0

            tot = A + B + carry
            dis = str(tot % 2)

            
            sum = sum + dis
            carry = tot // 2
        sum = sum[::-1]
        if carry == 1:
            return "1" + sum
        return sum
            
