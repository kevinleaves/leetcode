optimal solution: iterate from the back
3 pointers: 2 read pointers, 1 write pointer
​
// r1 at the end of nums1 m
// r2 at the end of nums2 n
// w at the end, total length of nums1
//# at write pointer is max btwn r1 and r2 values
//if r2 exhausted but not r1
//if r1 exhausted but not r2