class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        k is equal to the return array length

        count frequency of elements in nums
        return the k highest frequency elements in nums



        0  1 2 3 4
        [][3][2][1][]

        init counter dict
        populate counter dict with frequencies
        generate bucket array from dict using max value/frequency from dictionary
        populate bucket array with elements from nums
        iterate backwards from the bucket, populating result array and decrementing k until it reaches 0

        return res array
        '''
        counter = {}
        for num in nums:
          counter[num] = counter.get(num, 0) + 1
        
        maxFrequency = max(counter.values())
        
        buckets = [[] for _ in range(maxFrequency)]

        for key, value in counter.items():
          buckets[value - 1].append(key)

        res = []
        for i in range(len(buckets) -1, -1, -1):
          for j in range(len(buckets[i]) - 1, -1, -1):
            if k > 0:
              res.append(buckets[i][j])
            k -= 1          

        return res

        
