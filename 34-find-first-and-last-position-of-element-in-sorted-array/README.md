mistake that you made:
trying to make the algorithm work in only 1 binary search pass

you can run it twice lmao
2logn is still logN

found target => we need to find leftmost index that matches target.
found target => we need to find rightmost index that matches target.

normally we would return mid if we've found the target, but the bsearch can continue if you just update pointers

do this twice and store the indices of the leftmost and rightmost indices
return [left, right] if found otherwise if we've never come into contact with them return [-1,-1]
