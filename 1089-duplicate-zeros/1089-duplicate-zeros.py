class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.

        see a 0, duplicate the 0
        see a 0, store next number

        i: arr int 0-9
        o: same arr modified in place
        c: O(1) space, no time constraints
        e: 

        """
        possibleDups = 0
        last = len(arr) - 1

        # Find the number of zeros to be duplicated
        for left in range(last + 1):

            # Stop when left points beyond the last element in the original list which would be part of the modified list
            if left > last - possibleDups:
                break

            # Count the zeros
            if arr[left] == 0:
                
                # Edge case: zero at cutoff can't be duplicated. We have no more space, as left is pointing to the last element which could be included  
                if left == last - possibleDups:
                    arr[last] = 0 # For this zero we just copy it without duplication.
                    last -= 1
                    break
                possibleDups += 1
        
        left = last - possibleDups
        for i in range(left, -1, -1):
            # use possibleDups to calculate a dynamic index. we can't store the i + possibleDups calculation in a separate variable because it wouldn't update
            if arr[i] == 0:
                # update array and move to the left
                arr[i + possibleDups] = 0
                possibleDups -= 1
                arr[i + possibleDups] = 0
            else:
                arr[i + possibleDups] = arr[i]