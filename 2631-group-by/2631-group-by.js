/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
  // fn determines the groups/keys of the json
  // each group has an array as value, within it are the objects from initial array
  let res = {}
  
  // 1 pass to initialize arrays
  for (let i = 0; i < this.length;i++) {
    let element = this[i]
    // populate res with keys
    let key = fn(element)
    if (res[key] === undefined) {
      res[key] = []
    }
    res[key].push(element)
  }
  return res
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */