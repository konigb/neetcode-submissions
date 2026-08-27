class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # If char is a digit add to stack
        # If char is not a digit then pop 2 sum and add res to stack
        # return the final result

        stack = []

        for c in tokens:
            if c == "/":
                a, b = stack.pop(), stack.pop() 
                stack.append(int(float(b)/a))
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop() 
                stack.append(b - a)
            else:
                stack.append(int(c))
        return stack[0]

        