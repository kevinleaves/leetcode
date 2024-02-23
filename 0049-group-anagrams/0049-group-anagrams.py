class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        if two strings are anagrams, group them together in a subarray

        somehow need to hash a particular anagram pattern inside of a key. add any strings in strs
        that match the hash into its array

        we can represent a specific anagram pattern through an array of 26

        create hashtable to store our resulting arrays
        shape = {
          anagramPattern: ['eat', 'ate', 'tea'] 
          anagramPattern: [] 
          anagramPattern: [] 
        }
        iterate through strs
        for each string:
          generate a pattern array
          check for inclusion within our dict
          if our pattern is a key in the dict:
            add the current string to the array at that key
          otherwise
            create the key
            add the current string to the array at that key
        
        return array of all values in the hashtable
        '''

        grouped = {}
        for s in strs:
          pattern = [0]*26
          for c in s:
            pattern[ord(c) - 97] += 1
           
          # add to our hash
          key = str(pattern)
          if key not in grouped:
            grouped[key] = []  

          grouped[key].append(s)
        return grouped.values()


