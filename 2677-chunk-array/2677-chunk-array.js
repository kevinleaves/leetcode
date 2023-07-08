/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    if (arr.length === 0) return []
    if (size > arr.length) return [arr]

    // slice until no more chunks can be made
    let res = []
    let index = 0

    console.log(arr.slice(index, size))
    while (index < arr.length) {
      res.push(arr.slice(index, index + size))
      index += size
    }

    return res
};
