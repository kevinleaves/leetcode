/**
 * @param {Object | Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    // i: object or array
    // o: boolean stating whether the object is empty
    // c: O(1) time additional constraint
    // e: empty obj {} => true. empty array [] => true

    // O(n) solution(s)
    // const res = Array.isArray(obj) ? obj.length === 0 : Object.keys(obj).length === 0
    // const res = JSON.stringify(obj).length === 2;

    // O(1) time because we're only checking if we can enter the loop. only ever 1 operation
    for (const _ in obj) {
      return false
    }
    return true
};