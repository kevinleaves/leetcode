/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
    /**
    i: multiple dimensional array arr + maxDepth n
    o: flattened version of the array
    c: none/cannot use Array.flat
    e: n === 0 => no flattening
     */
    if (n === 0) return arr

    let res = []
    let recurse = (arr, currDepth) => {
      for (const element of arr) {
        let withinRange = currDepth <= n && currDepth > 0
        if (Array.isArray(element) && withinRange) {
          recurse(element, currDepth - 1)
        } else {
          res.push(element)    
        }
      }
    } 
    recurse(arr, n)
    return res
};