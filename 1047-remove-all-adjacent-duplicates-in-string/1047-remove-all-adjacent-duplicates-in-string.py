class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                # if current char != top of stack char, add new pair to stack
                stack.append([char, 1])
            # check for duplicates and remove
            if stack[-1][1] == 2:
                stack.pop()
        
        res = ''
        for char, count in stack:
            res += (char * count)

        return res