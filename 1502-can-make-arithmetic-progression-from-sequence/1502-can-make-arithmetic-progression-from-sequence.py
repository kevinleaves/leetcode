class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        '''
        i: int[]
        o: bool (can we make an arithmetic progression from the input array)
        c: none
        e: can have negative progression

        sort array
        diff = 2
             l r
        [1 3 5]

        [4, 1, 10, 7] -> true
        '''
        
        arrSorted = sorted(arr)

        l, r, = 0, 1
        diff = arrSorted[r] - arrSorted[l]
        while r < len(arrSorted):
            if (arrSorted[r] - arrSorted[l]) != diff:
                return False

            l += 1
            r += 1

        return True
        