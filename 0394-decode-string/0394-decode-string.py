class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        for i in s:
            if i == ']':
                subS = ''
                while stack and stack[-1] != '[':
                    subS = stack.pop() + subS
                stack.pop()

                integer = ''
                while stack and stack[-1].isdigit():
                    integer = stack.pop() + integer
                stack.append((int(integer)*subS))
                
            else:
                stack.append(i)

        return ''.join(stack)