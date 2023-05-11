# 83.62% 11.53%
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]

        res = [0] * len(temperatures)
        stack = []

        # store tuples in stack (temp, i)
        for i in range(len(temperatures)):
            # curr temp
            currTemp = temperatures[i]
            # while loop to pop
            # if curr temp > top of stack temp, pop
            while stack and currTemp > stack[-1][0]:
                # compare current temperature to top of stack
                popped = stack.pop()
                res[popped[1]] = i - popped[1]
            stack.append((currTemp, i))
        return res
