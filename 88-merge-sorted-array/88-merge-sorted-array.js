/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
  //set pointers, m, n, m+n
  var last = m + n - 1;
  m = m-1
  n = n-1
  // console.log(last, m, n)
  //iterate backwards through nums1
  while (n >= 0) {
    if (nums1[m] > nums2[n]) {
      nums1[last] = nums1[m]
      m--
    } else {
      nums1[last] = nums2[n]
      n--
    }
    last--
  }
  
  
};