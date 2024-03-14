class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        '''
        init a dict/set to store key/value pairs
        iterate through items1, adding kv pairs

        iterate through items2
          if key in set, add curr item's val to the existing val
          if not in set, add to set

        generate 2d array from set/dict
        sort by k ascending order
        '''
        pairs = {}
        for value, weight in items1:
          pairs[value] = weight
        
        for value, weight in items2:
          if value in pairs:
            pairs[value] += weight
          else:
            pairs[value] = weight

        res = list(pairs.items())

        res.sort(key=lambda pair: pair[0])
        
        return res
