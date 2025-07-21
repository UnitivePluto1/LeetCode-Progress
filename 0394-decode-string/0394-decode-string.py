class Solution:
    def decodeString(self, s: str) -> str:
        subS = ''
        stack = []
        for i in s:
            if i == ']':
                while stack and stack[-1] != '[':
                    subS = stack.pop() + subS
                stack.pop()

                integer = ''
                while stack and stack[-1].isdigit():
                    integer = stack.pop() + integer
                stack.append((int(integer)*subS))
                subS = ''
            else:
                stack.append(i)

        return ''.join(stack)