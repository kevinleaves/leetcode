class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def sortByPosition(tuple):
            return tuple[0]

        tuples = [0] * len(position)
        for i in range(len(position)):
            tuples[i] = (position[i], speed[i])

        tuples.sort(key=sortByPosition)
        # print('tuples: ', tuples)
        stack = []

        for i in range(len(tuples) - 1, -1, -1):
            car = tuples[i]
            # calculate T
            t = (target - car[0]) / car[1]
            stack.append([car, t])

            # conditional: if top stack car faster pop it
            if len(stack) >= 2 and t <= stack[-2][1]:
                stack.pop()

            # print(stack)
        return len(stack)
