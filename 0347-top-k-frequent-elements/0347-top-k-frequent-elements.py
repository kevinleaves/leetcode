class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        I: int[]
        O int[] with the top k most frequent elements in nums
        C: nums len > 0. time is better than O(nlogn). no space constraints
        E: k is always valid. 


        initial object to store frequencies
        create bucket array
        iterate over that object's keys, create a new bucket array in buckets using value at key.
        append current key to that bucket if it exists

        create res array
        iterate through buckets array backwards,
        appending items from the highest frequency bucket until res array length == k

        return k
        '''

        freq = collections.defaultdict(int)
        for num in nums:
            freq[num] += 1

        buckets = []

        for i in range(max(freq.values()) + 1):
            buckets.append([])

        for key in freq.keys():
            val = freq[key]
            buckets[val - 1].append(key)
        
        # iterate through buckets backwards until we find k amount
        res = []

        for i in range(len(buckets) - 1, -1, -1):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
                if len(res) == k:
                    return res
    


