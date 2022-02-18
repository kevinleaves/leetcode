class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #l, r pointers
        #while loop stops when l > r
        #while loop runs when l <= r
        l, r = 0, len(numbers)-1
        while l <= r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
                print(f"l = {l}")
            else:
                r -= 1
                print(f"r = {r}")
        
        
                