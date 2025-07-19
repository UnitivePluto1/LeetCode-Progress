class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        word = ""
        for letter in s:
            if len(stack) == 0:
                stack.append(letter)
                continue
            if stack[-1] != letter:
                stack.append(letter)
            else:
                stack.pop()
                continue
        while stack:
            word += stack.pop()
        return word[::-1]