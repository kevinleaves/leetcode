class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
      '''
      part 1: find idx of ch
      if idx not found, return original word
      part 2: reverse that prefix
      '''
      right = -1
      for i, c in enumerate(word):
        if c == ch:
          right = i
          break

      if right == -1:
        return word

      left = 0
      chArray = list(word)
      while left <= right:
        chArray[left], chArray[right] = chArray[right], chArray[left]
        left += 1
        right -= 1

      return ''.join(chArray)



