class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        i: 2 strings of lowercase english chars
        o: merged string
        c: none
        e: 3 cases (w1 larger w2 larger, both equal length)

        
           2
        "abv" 
        
           2
        "pq"

        merged = 'a'
        '''

        position = 0
        merged = ''
        while position < len(word1) and position < len(word2):
            merged += word1[position]
            merged += word2[position]
            position += 1
        
        # if w1 is shorter, add rest of w2
        if position >= len(word1):
            merged += word2[position:]
        # if w2 is shorter, add rest of w1
        else:
            merged += word1[position:]

        return merged
