class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        '''
        i: 2d array nums. at each index is a car. car includes range that it covers within the line
        o: int representing the # of points that are covered by all the cars. from 1 -> max(nums)
        c: none
        e: numbers cannot be negative. nums len >= 1

        total int points on the line are in the range 1 to max int in nums
        how many of these points are covered


        {1,2,3,5,6,7,8}
        '''
        # O(N x M) time, where N is the number of cars, and M is the maximum distance that the car covers
        # O(N) space

        # initialize a set
        points = set()
        # iterate through nums, 
        for car in nums:
          # at each car array, iterate through that car's start and end range (inclusive)
          for point in range(car[0], car[1]+1):
            #  add point to the set
            points.add(point)

        # return length of set
        return len(points)

