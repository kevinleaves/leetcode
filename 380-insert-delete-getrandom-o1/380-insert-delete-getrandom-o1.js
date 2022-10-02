
var RandomizedSet = function() {
    this.map = {};
    this.list = [];
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function(val) {
    if (this.map[val] !== undefined) {
      return false
    } 
    this.map[val] = this.list.length;
    this.list.push(val)
    return true
  };

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function(val) {
    let res = val in this.map
    if (res) {
      let idx = this.map[val];
    //replace value at array with last value
      let lastVal = this.list[this.list.length-1];
      this.list[idx] = lastVal
      this.list.pop()
      this.map[lastVal] = idx
    
      delete this.map[val]    
    }
    //store removed value index
    
    return res
};

/**
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function() {
    if (this.list.length === 0) {
      return null
    }
    return this.list[Math.floor(Math.random() * this.list.length)]
};

/** 
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */