class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    # create freq table out of magazine (these are the available letters)
    magazineFreq = {}
    for c in magazine:
      magazineFreq[c] = magazineFreq.get(c, 0) + 1
    
    # iterate through ransomnote
    for c in ransomNote:
      # if randomNote[i] is not in magazine
        # return false
      # if randomNote[i] is not > 0
        # return false
      if c not in magazineFreq or magazineFreq[c] <= 0:
        return False
      # decrement 1 frequency from that letter
      magazineFreq[c] -= 1
    
    # if we complete iteratation, return true
    return True