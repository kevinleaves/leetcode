class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        '''
        i: string 
        o: string after all operations performed 
        c: none
        e: operations can always be performed

        stack = [lecoe]
                       i
        s = "leet**cod*e"

        '''

        for char in s:
            if char == '*' and stack:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
