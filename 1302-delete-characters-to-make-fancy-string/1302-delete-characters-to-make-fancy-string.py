class Solution:
    def makeFancyString(self, s: str) -> str:
        cnt = 0

        last = new = ''

        for i in s:
            if i == last:
                cnt += 1
            else:
                cnt = 1

            if cnt <= 2:
                new += i
            last=i
        return new