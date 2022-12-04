/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
  var shorterArr;
  
    //only iterate the shorter length array
    if (nums1.length < nums2.length) {
      shorterArr = nums1;
    } else {
      shorterArr = nums2;
    }
  
    //build freq tables for each
  var freq1 = {};
  var freq2 = {};
  
  nums1.forEach(function (item) {
    freq1[item] = (freq1[item] || 0) + 1;
  });
  nums2.forEach(function (item) {
    freq2[item] = (freq2[item] || 0) + 1;
  });
  
    //res array to store answer  
  var res = [];
  
    //iterate through shorter array
  shorterArr.forEach(function (item) {
      //check freq table if has both
    if (item in freq1 && item in freq2) {
      //if it does, add to res
      res.push(item)
      //decrement freq table, delete the key if freq hits 0
      freq1[item]--
      if (freq1[item] === 0) {
        delete freq1[item]
      }
      freq2[item]--
      if (freq2[item] === 0) {
        delete freq2[item]
      }
    }
  });
    
  return res
};