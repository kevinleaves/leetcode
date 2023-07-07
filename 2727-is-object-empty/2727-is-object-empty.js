/**
 * @param {Object | Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    // i: object or array
    // o: boolean stating whether the object is empty
    // c: O(1) time additional constraint
    // e: empty obj {} => true. empty array [] => true

    const res = Array.isArray(obj) ? obj.length === 0 : Object.keys(obj).length === 0
    return res
};