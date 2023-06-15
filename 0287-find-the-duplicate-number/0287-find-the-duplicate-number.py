class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # slow and fast == first index of nums
        slow, fast = 0, 0
        # basically a do-while loop
        while True:
            # slow is set to whatever it points at
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            # update slow2
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow2
