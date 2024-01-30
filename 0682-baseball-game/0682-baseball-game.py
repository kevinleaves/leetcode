class Solution:
    def calPoints(self, operations: List[str]) -> int:
        '''
        i: operations array
        o: int (sum of all scores on the record after applying all ops)
        c: no invalid operations will be performed 
        e: 
        
        if element is not C D or +, it's a number
        
        create stack
        iterate through ops:
          if C: pop
          elif D: peek at number, double it, append result
          elif +: peek 2, add them, append result
          else number: append

        at the end:
        iterate stack pop to sum result,
        return result
        '''

        stack = []
        for op in operations:
          # check for ops
          if op == "C":
            stack.pop()
          elif op == "D":
            stack.append(stack[-1]*2)
          elif op == '+':
            stack.append(stack[-1] + stack[-2])
          else:
            stack.append(int(op))
        
        res = 0
        for i in range(len(stack)):
          res += stack.pop()

        return res


