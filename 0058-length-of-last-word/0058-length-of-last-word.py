class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''
        i: string of a-z chars + # spaces
        o: int representing the length of the last word in the string
        c: none
        e: strings can have multiple spaces btwn words

        split on space => take array last index => find length
        string split doesn't work fully when space delimiter > 1 space. NVM IT DOES
        '''
        split = s.split()
        return len(split[-1])