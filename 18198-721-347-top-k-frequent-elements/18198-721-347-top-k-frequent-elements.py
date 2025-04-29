class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      # make freq
      freq = {}
      for n in nums:
        freq[n] = freq.get(n, 0) + 1
      
      # make buckets
      # max frequency of any number is the size of the nums array
      buckets = [[] for n in range(len(nums) + 1)]
      
      for key in freq:
        val = freq[key]
        buckets[val].append(key)
      
      # iterate through buckets from right to left, until appended
      # k elements to res
      print(buckets)
      print(freq)
      res = []
      for i in range(len(buckets) - 1, 0, -1):
        for n in buckets[i]:
          res.append(n)
          if len(res) == k:
            return res