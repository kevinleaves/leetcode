# 17.93% 7.59%
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        # append numbers to stack. once we encounter an operator,
        # pop 2 numbers off stack
        # perform operation,
        # append back on stack & continue

        operators = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                right_operand = stack.pop()
                left_operand = stack.pop()
                if token == "+":
                    stack.append(left_operand + right_operand)
                if token == "-":
                    stack.append(left_operand - right_operand)
                if token == "*":
                    stack.append(left_operand * right_operand)
                if token == "/":
                    stack.append(int(left_operand / right_operand))
        return stack[-1]
