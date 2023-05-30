class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # l, r pointers at beginning and end
        l, r = 0, len(people) - 1
        # sort input array
        people.sort()
        # res count variable
        res = 0
        # while loop
        while l <= r:  # or could be <=
            # largest people get their own boat by default
            while people[r] == limit:
                # decrement r
                r -= 1
                # increment res
                res += 1
            # 2 ppl too heavy for 1 boat
            while people[r] + people[l] > limit and l <= r:
                r -= 1
                res += 1
            # 2 ppl fit in 1 boat
            while people[l] + people[r] <= limit and l <= r:
                l += 1
                r -= 1
                res += 1

        return res
