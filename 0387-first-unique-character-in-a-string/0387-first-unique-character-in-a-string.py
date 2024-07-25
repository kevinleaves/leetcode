class Solution:
  def firstUniqChar(self, s: str) -> int:
    # char: last found index
    # {l: 1, e:3, t:1, c:1, o:1, d:1}
    res = -1
    freq = {}
    for c in s:
      freq[c] = freq.get(c, 0) + 1
    
    for i, c in enumerate(s):
      if freq[c] == 1:
        res = i
        break

    return res

          
