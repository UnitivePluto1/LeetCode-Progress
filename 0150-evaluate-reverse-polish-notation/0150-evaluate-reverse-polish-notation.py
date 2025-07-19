class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def comp(num1,num2,op):
            match op:
                case '+':
                    return num1 + num2
                case '-':
                    return num1-num2
                case '*':
                    return num1* num2
                case '/':
                    return int(num1 / num2)

        stack = []
        op = ['+','-','*','/']
        for i in tokens:
            if i in op:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(comp(num1,num2,i))
            else:
                stack.append(int(i))
        return int(stack.pop())
