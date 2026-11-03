class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opers = {"+", "-", "*", "/"}
        for x in tokens:
            if x not in opers:
                stack.append(x)
            elif x in opers:
                second = int(stack.pop())
                first = int(stack.pop())
                if (x == "+"):
                    stack.append(second + first)
                elif (x == "/"):
                    stack.append(first/second)
                elif (x == "*"):
                    stack.append( first * second)
                else:
                    stack.append ( first - second)
        
        return int(stack[0])


