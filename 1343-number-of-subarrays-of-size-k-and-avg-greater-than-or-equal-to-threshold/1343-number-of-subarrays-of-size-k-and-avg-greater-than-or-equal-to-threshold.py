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
