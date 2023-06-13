/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
  // i: 2 promises
  // o: 1 promise that resolves with the value of adding the 2 numbers
  
  // individual awaits work but this is too blocking. want promises to resolve simulateously 
  // const res1 = await promise1
  // const res2 = await promise2
  
  // resolve the 2 promises, add them up, create a new promise that resolves with the sum
  const resolved = await Promise.all([promise1, promise2])
  
  return new Promise(resolve => resolve(resolved.reduce((accum, item) => {
      return accum + item
  }, 0)))
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */