class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        idx = 1
        flowerbed2 = [0] + flowerbed + [0]
        
        while idx < len(flowerbed2) - 1:
            if flowerbed2[idx] == 1:
                idx += 2
            else:
                # check adjacent plots for 1's
                if flowerbed2[idx - 1] != 1 and flowerbed2[idx + 1] != 1:
                    # we can fill 
                    flowerbed2[idx] = 1
                    n -= 1
                    idx += 2
                else:
                    idx += 1
        return n <= 0
