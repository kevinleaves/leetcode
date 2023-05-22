class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = int(l + (r - l) / 2)
            currH = 0
            for pile in piles:
                currH += ceil(pile / k)
            # if currH == h:
            #     return k
            if currH <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res
        # bsearch the range between 1 and max(piles) for k
        # for each possible rate k, calculate the amount of time it takes to eat bananas (h)
        # if calculated h is == input h, we've found an eating speed that works, but we don't know if it's the min yet. we need to search lower bounds. chop off upper range
        # if calculated h is < input h, we're eating too fast. chop off upper range
        # if calculated h is > input h, we're eating too slow. chop off lower range

        # ultimately we use condition of currH <= h
