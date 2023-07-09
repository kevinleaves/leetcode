/**
 * @param {Object} obj
 * @return {Object}
 */
var compactObject = function(obj) {
        /**
    i: obj/array
    o: obj with keys that contain falsy values removed
    c: no time/space constraints
    e: 
    */
    
    // is array
    /**
    build res obj
    if is array
    iterate thru elements
    if ele is not obj
        push to res if truthy
    else (it is obj)
        recursive call
    */
    
    
    function dfs(obj) {
      // base case(s)
      if (!obj) return false
      if (typeof obj !== 'object') return obj 

      // recursive case(s)
      // if array
      if (Array.isArray(obj)) {
        // build newArr
        let newArr = []

        for (let i = 0; i < obj.length; i++) {
            const element = obj[i];
            let subArr = dfs(element)
            if (subArr) {
              newArr.push(subArr)
            }
        }

        return newArr
      } else {
        // if pojo, build newObj
        let newObj = {}
        for (const key in obj) {
          // if obj[key] is truthy, add to new obj
          const val = obj[key]
          const subObj = dfs(val)
          if (subObj) {
            newObj[key] = subObj
          }
        }

        return newObj
      }
    } 

    return dfs(obj)
};