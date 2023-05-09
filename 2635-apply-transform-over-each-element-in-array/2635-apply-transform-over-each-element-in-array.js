var map = function (arr, fn) {
  let result = [];
  for (let i = 0; i < arr.length; i++) {
    let element = arr[i];
    result.push(fn.call(this, element, i));
  }

  return result;
};

// better to make a new array w/ static length.
// Preallocate Memory
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function (arr, fn) {
  let newArray = new Array(arr.length);
  for (let i = 0; i < arr.length; i++) {
    newArray[i] = fn.call(this, arr[i], i);
  }

  return newArray;
};
