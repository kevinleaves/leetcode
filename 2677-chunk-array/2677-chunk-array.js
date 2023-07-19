/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    /**
    i: arr<int> size int
    o: arr<arr int>

    []
          
    [1,2,3,4,5]
     */
    if (arr.length === 0) {
      return []
    }

    if (arr.length < size) {
      return [arr]
    }

    let res = []
    let idx = 0

    while (idx < arr.length) {
      let chunk = arr.slice(idx, idx + size)
      idx += size
      res.push(chunk)
    }    
    
    return res
};
