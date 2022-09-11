/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) { //[0], 0, [1], 1
    //3 pointers
    let pos = m + n - 1 //0
    m = m - 1; //-1
    n = n - 1; //0
    
//     //we must traverse entirety of the second array from the right side
    while (n >= 0) { //n = 0 true
        //compare largest number of 2nd array & the first array
        if (nums1[m] > nums2[n]) {
            nums1[pos] = nums1[m];            
            m--;
        } else {
            nums1[pos] = nums2[n];
            n--
        }
        pos--;
    }
};

