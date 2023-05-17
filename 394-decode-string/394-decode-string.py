# 52.99% 7.54%
class Solution:
    def decodeString(self, s: str) -> str:
        # init a stack
        stack = []

        # iterate through encoded string
        for i, char in enumerate(s):
            if char == "]":
                subString = ""
                while stack[-1].isalpha():
                    subString = stack.pop() + subString

                # pop off the [
                stack.pop()

                # find digits & pop off digits
                digits = ""
                while stack and stack[-1].isnumeric():
                    digits = stack[-1] + digits
                    stack.pop()
                # multiply chunks & add back to stack
                for i in range(int(digits)):
                    stack.append(subString)
            else:
                stack.append(char)

        return "".join(stack)
