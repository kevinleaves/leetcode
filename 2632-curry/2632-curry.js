/**
 * @param {Function} fn
 * @return {Function}
 */

// recursive implementation
var curry = function (fn) {
  // store the original # of args

  return function curried(...args) {
    /**
    if # of args passed into curried is not === to the original number of args,
    return a curried fn with a partially applied arg

    base case: if we have the same # of arguments, call the original function.
    */
    if (args.length === fn.length) {
      return fn.apply(this, args);
    }

    return (...nextArgs) => curried(...args, ...nextArgs);
  };
};

// implementation with bind
var curry = function (fn) {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn.apply(this, args);
    }
    return curried.bind(this, ...args);
  };
};

/**
* function sum(a, b) { return a + b; }
* const csum = curry(sum);
* csum(1)(2) // 3

ex2:
const add = a => b => a + b;
const add5 = add(5)
const res = add5(3)
console.log(res) // 8
*/

// i: fn
// o: curried fn OR the same value as the original function would have returned
// c:
// e:
