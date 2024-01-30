class Solution:
    def isValid(self, s: str) -> bool:
        '''
        i: string with various bracket characters
        o: boolean. true if input string is valid.
        c: o(n) time? no space constraints
        e: s length could be 1. odd s length vs even s length

        how do we know that we use a stack?
        order of operations.
        check for validity by iterating through a string or an array. like a calculator or checking for valid brackets. 
        pattern: 
        if x happens, pop, else push, etc. etc.
        can determine answers based on remaining length of stack after operations, sum of items remaining in stack, etc
        '''

        stack = []
        brackets = dict([
          (')', "("),
          ('}', "{"),
          (']',"["),
        ])

        for char in s:
          # if char is an open bracket, push to stack
          if char not in brackets:
            stack.append(char)

          # otherwise:
          else:
            # peek stack, if closing bracket doesn't correspond,
            if len(stack) == 0 or brackets[char] != stack[-1]:
              return False
            else:
              stack.pop()
        
        return len(stack) == 0 
            
