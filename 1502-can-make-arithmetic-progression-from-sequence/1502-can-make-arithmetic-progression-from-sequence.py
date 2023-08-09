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


        no sorting
        use set
        store differences in set
        store initial diff in set
        before adding to set, check inclusion, if diff isn't in set, return false
        '''

        min_value, max_value = min(arr), max(arr)
        n = len(arr) 
        
        # if min and max value are the same, every element is the same, return True
        if max_value - min_value == 0:
            return True
        
        # can think of n - 1 as # of gaps in the array. [3, (GAP) 5, (GAP) 1] 5 - 1 % 2 -> 0
        if (max_value - min_value) % (n - 1) != 0:
            return False
        
        # establish an initial diff we use to determine the result
        diff = (max_value - min_value) // (n - 1)


        number_set = set()
        
        for a in arr:
            if a in number_set:
                return False
            if (a - min_value) % diff != 0:
                return False
            number_set.add(a)
        
        return True