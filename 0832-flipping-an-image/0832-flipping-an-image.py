class Solution:
    def flipRow(self, row: List[int]) -> None:
      left = 0
      right = len(row) - 1
      while left < right:
        row[left], row[right] = row[right], row[left]
        left += 1
        right -= 1
      return row

    def invertRow(self, row: List[int]) -> None:  
      for i, v in enumerate(row):
        if v == 0:
          row[i] = 1
        else:
          row[i] = 0
      return row

    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
      '''
      for each subarray:
        reverse each subarray
        then invert
      '''
      for row in image:
        self.invertRow(self.flipRow(row))
  
      return image