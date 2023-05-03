class Solution:
    def isValid(self, s: str) -> bool:
        # i: string that contains bracket chars
        # o: boolean representing if input string is valid.
        # c: none
        # e: s length == 0?

        # odd length strings auto false
        if len(s) % 2 == 1:
            return False

        mapping = {")": "(", "]": "[", "}": "{"}

        stack = []

        for c in s:
            # if open bracket, add to stack
            if c not in mapping:
                stack.append(c)
            else:
                # if close bracket, check top stack is matching bracket
                if len(stack) == 0 or mapping[c] != stack.pop():
                    return False

        return len(stack) == 0


# 9.38 5.79%
