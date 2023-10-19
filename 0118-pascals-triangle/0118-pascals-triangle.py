class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        i loops from 0 -> 3 because we've already filled the first subarray. i iterates 4 times
        j loops subarray length. append j times.

        my way:
        we loop based on positions

        i iterates from 1 to 4, representing the res array slots to fill
        j iterates 0 to length of subarray, filling in slots at index j


        '''

        res = [[1]]

        for i in range(1, numRows):
            temp = [0] + res[i - 1] + [0] # pad outer with extra 0s. 
            curr = [1] * (len(res[i - 1]) + 1)
            for j in range(len(curr)):
                curr[j] = temp[j] + temp[j + 1]

            res.append(curr)

        return res