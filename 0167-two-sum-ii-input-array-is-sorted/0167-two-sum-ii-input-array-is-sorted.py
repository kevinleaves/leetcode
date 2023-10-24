class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force solution -> n^2. this is part of the constraint
        # binary search
        l, r = 0, len(numbers) - 1
        while l < r: # breaks when they're both equal
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l + 1, r + 1]
            elif sum < target:
                l += 1
            else:
                r -= 1
        

        
