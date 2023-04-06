problems:
i can't decide where the pointers start. possibly both start at 0?
i can't think of the logic to move pointers.
i can't think of the logic to calculate how much water is between two walls.

min of max left and max right at each position

use 2 pointers starting from both sides
store max L and max R values.
at every position, add to res based on the formula:
min(maxL, maxR) - height[currPosition]
