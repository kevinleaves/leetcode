class Solution:
    def reverseWords(self, s: str) -> str:
        #2 pointers
        #count whitespace
        #split string
        #reverse all strings
        #return them all added together + whitespace
    
        new = []
        for i in s.split(" "):
            i = i[::-1]
            new.append(i)
        return " ".join(new)