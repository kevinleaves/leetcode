/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function (fn) {
  let numberOfCalls = 0;
  return function (...args) {
    if (numberOfCalls === 0) {
      numberOfCalls += 1;
      return fn.apply(this, args);
    } else {
      return undefined;
    }
  };
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */

// i: function
// o: the same function but decorated with constraint that it can only be called once. subsequent calls return undefined
