/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {

// p1 at the end of nums1 m
  var r1 = m-1;
  var r2 = n-1;
  var w1 = m + n - 1;
// p2 at the end of nums2
// p at the total length of nums1
  
  //while both read pointers haven't been exhausted yet:
  while (r1 >= 0 && r2 >= 0) {
    //# at write pointer is max btwn r1 and r2 values
    //r2 > r1
    if (nums2[r2] > nums1[r1]) {
      nums1[w1--] = nums2[r2--]; 
    //r2 <= r1
    } else {
      nums1[w1--] = nums1[r1--];
    }
  }
  
  //if r2 exhausted but not r1
  while (r2 >= 0) {
    nums1[w1--] = nums2[r2--]
  }
  
  return nums1
};