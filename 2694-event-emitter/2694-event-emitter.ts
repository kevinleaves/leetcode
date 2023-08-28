type Callback = (...args: any[]) => any;
type Subscription = {
    eventName: string
    callback: Callback
    unsubscribe: () => void
}

/**
EventEmitter object has field to store key:values
subscribing to an event -> store event name: [array of callbacks passed into this event]
emit(event) => iterates through

 */
class EventEmitter {
  // object to store k:v pairs
  data = {}

  subscribe(eventName: string, callback: Callback): Subscription {
    if (!this.data[eventName]) this.data[eventName] = []
    this.data[eventName].push(callback)

    return {
    // constructor method, sets fields for eventName and callback
    eventName: eventName,
    callback: callback,
    
    // uses fields to populate global data obj
      unsubscribe: () => {
        // accesses eventEmitter object through closure.
        // Subscription object has a field containing its event name and callback
        // removes callback from global event array
        const idx = this.data[eventName].indexOf(callback)
        this.data[eventName].splice(idx, 1)
      }
    };
  }

  
  emit(eventName: string, args: any[] = []): any[] {
    // accesses array at key eventName:
    const cbs = this.data[eventName]
    // if empty array, return []
    if (!cbs) return [] 
    // instantiate res []
    const res = [];
    // iterates through array of cbs, 
    for (let i = 0; i < cbs.length; i++) {
      const cb = cbs[i];
      res.push(cb.apply(null, args))
    }
    // passes args into cbs, calls cbs
    // add cb result into res array
    // return res array  
    return res
  }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */

