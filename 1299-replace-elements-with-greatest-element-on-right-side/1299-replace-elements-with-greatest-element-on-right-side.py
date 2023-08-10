class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''
        i:
        o: 
        c: in place? modify input array O(1) space. has to be more efficient than n^2
        
        Input: arr = [17,18,5,4,6,1]

        maxNum = 18
        currVal = 17
        i = 0
        res = [18,6,6,6,1,-1]
        '''

        # this is an n^2 solution
        '''
        for i in range(len(arr) - 1):
            maxNum = max(arr[i+1:])
            arr[i] = maxNum

        arr[-1] = -1
        return arr
        '''

        maxNum = 0
        for i in range(len(arr) - 1, -1, -1):
            curr = arr[i]
            arr[i] = maxNum
            maxNum = max(maxNum, curr)
            if i == len(arr) - 1:
                arr[i] = -1

        return arr