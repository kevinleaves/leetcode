class Solution:
    def calPoints(self, ops: List[str]) -> int:
        points = 0

        if len(ops) == 1:
            return int(ops[0])

        stack = []

        for op in ops:
            if op == "C":
                points -= stack.pop()
            elif op == "D":
                doubled = stack[-1] * 2
                stack.append(doubled)
                points += doubled
            elif op == "+":
                summed = stack[-1] + stack[-2]
                stack.append(summed)
                points += summed
            else:
                score = int(op)
                stack.append(score)
                points += score

        return points
