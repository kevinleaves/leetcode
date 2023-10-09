class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # dictionary to hold character: frequency that character occurs in s
        frequency = {}

        # iterate through chars of s
        for c in s:
            # update key with current frequency
            frequency[c] = frequency.get(c, 0) + 1
        
        print(frequency)
        for c in t:
            if c not in frequency or frequency[c] <= 0:
                return False
            else:
                frequency[c] -= 1

        return True
                


        