class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        '''
        i: 2d array
        o: boolean
        c:
        e:
        Input: matrix = 
        [
        0,0   
        [1,2,3,4],
        [5,1,2,3], 1, 1
        [9,5,1,2]  2, 2
        ]

        '''
        R = len(matrix)
        C = len(matrix[0])

        # traverse original col
        for row in range(R):
            first = matrix[row][0]
            for col in range(1, C):
                # traverse diagonal from first
                if row + col < R and col < C:
                    next = matrix[row + col][col]
                    if first != next:
                        return False


        # traverse original row
        for col in range(C):
            first = matrix[0][col]
            for row in range(1, R):
                if row + col < C and row < R:
                    next = matrix[row][row + col]
                    if first != next:
                        return False

        return True

'''
[
[11,74,0,93],
[40,11,74,7]
]
'''





        