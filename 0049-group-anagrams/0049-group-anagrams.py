class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for string in strs:
            # key is an empty array of length 26
            keyArray = [0]*26
            # iterate through current string
            for c in string:
                # for each character, increment the correct position in the array
                keyArray[ord(c) - 97] += 1                

            key = tuple(keyArray)
            if  key not in hash:
                hash[key] = []
                # add the current string to the array
                # append the current string to the array
                
            hash[key].append(string)

        # grab all subarrays from the hashmap and return them
        return hash.values()