/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function (arr, fn) {
  let res = [];
  // loop over array
  for (let i = 0; i < arr.length; i++) {
    // call fn on each element
    let evaled = fn(arr[i], i);
    if (evaled) {
      res.push(arr[i]);
    }
  }
  // returned array contains elements that evaluate to truthy
  return res;
};

// preallocate memory
function filter(arr: number[], fn: (n: number, i: number) => any): number[] {
  let size = 0;
  const newArr: number[] = new Array(arr.length);
  for (let i = 0; i < arr.length; ++i) {
    if (fn(arr[i], i)) {
      newArr[size] = arr[i];
      size++;
    }
  }
  // Ensure new array is of length size
  while (newArr.length > size) {
    newArr.pop();
  }
  return newArr;
}
