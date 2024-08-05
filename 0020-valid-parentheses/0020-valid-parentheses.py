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

      if odd length string, immediately return false
      '''

      if len(s) % 2 == 1:
        return False

      # create a mapping
      # create a stack
      stack = []
      mapping = {
        "]": "[",
        ")": "(",
        "}": "{",
      }
      # s = "}{" => false -> encounter closing bracket when stack is empty
      # s = "(){" => false -> odd length s
      # s = "(){{" => false -> stack isn't empty at end of iteration
      # s = "(]" => closing bracket doesn't match top of stack
      
      # iterate through s
      for c in s:
        # if close bracket
        if c in mapping:
          # check top of stack to see if it's a pair
          if len(stack) == 0:
            return False
          # if not,
            # return false
          if stack[-1] != mapping[c]:
            return False
          stack.pop()
        # if open bracket, add to stack
        else:
          stack.append(c)
      # if stack is empty, return true, else false
      

      return len(stack) == 0
        
