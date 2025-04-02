class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digs = len(digits)

        if digits[digs-1] < 9:
                digits[digs-1] = digits[digs-1] + 1
                return digits

        for i in range(digs-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits