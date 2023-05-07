/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */

class Counter {
  constructor(init) {
    this.init = init;
    this.currentNumber = init;
  }

  increment() {
    return ++this.currentNumber;
  }

  decrement() {
    return --this.currentNumber;
  }

  reset() {
    this.currentNumber = this.init;
    return this.init;
  }
}

var createCounter = function (init) {
  return new Counter(init);
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */

// closure w/ proxy
var createCounter = function (init: number) {
  let currentCount = init;
  return new Proxy(
    {},
    {
      get: (target, key) => {
        switch (key) {
          case 'increment':
            return () => ++currentCount;
          case 'decrement':
            return () => --currentCount;
          case 'reset':
            return () => (currentCount = init);
          default:
            throw Error('Unexpected Method');
        }
      },
    }
  );
};
