# 16.5% 52.1%
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        l = 0
        total = 0
        for r in range(len(arr)):
            total += arr[r]
            # contract window/shift l pointer
            # print(arr[l:r+1])
            if r - l + 1 > k:
                # if len(arr[l:r+1]) > k:
                # increment l
                total -= arr[l]
                l += 1
            # expand window/shift r pointer
            # window is k length, calculate avg
            if r - l + 1 == k:
                # if len(arr[l:r+1]) == k:
                # total = sum(arr[l:r+1])
                # avg = total/len(arr[l:r+1])
                avg = total / (r - l + 1)
                if avg >= threshold:
                    res += 1
        return res


# 79.43% 31.27%
# checks edge case + initializes a total + valid subarray right away
# every iteration of the loop slides window. calculates back of the window using the right pointer
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        # edge case: if length of arr < k, no valid subarrays
        if len(arr) < k:
            return res
        # initialize total at a valid k to immediately skip over subarrays < size k
        windowTotal = sum(arr[:k])
        # check initial total
        if windowTotal >= threshold * k:
            res += 1

        # begin a loop starting from k to the end of the array, sliding the window at every iteration
        for r in range(k, len(arr)):
            # add right to total
            windowTotal += arr[r]
            # increment left/contract the window/total. calculate the left of the window using the right pointer
            windowTotal -= arr[r - k]

            # check if window is valid
            if windowTotal >= threshold * k:
                res += 1

        return res
