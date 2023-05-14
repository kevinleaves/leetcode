/**
 * @param {Function} fn
 */
function memoize(fn) {
  let cache = {};
  return function (...args) {
    const key = JSON.stringify(args);
    // check cache for unique arg key, if found, return cached result
    if (key in cache) {
      return cache[key];
    } else {
      // otherwise execute fn, store the arg:result as a key:value pair in cache
      const result = fn.apply(this, args);
      cache[key] = result;
      return result;
    }
  };
}

/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */
