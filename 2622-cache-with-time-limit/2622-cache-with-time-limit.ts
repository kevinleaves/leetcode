class TimeLimitedCache {
    
    data = new Map()

    constructor() {
    }
    
    set(key: number, value: number, duration: number): boolean {
        // attempt to get from data
        const get = this.data.get(key)

        // cb that deletes a key from the data after timeout ends


        let ref = setTimeout(() => {
            this.data.delete(key)
        }, duration)

        if (get) {
            // returns true if unexpired key exists
            // exists, we need to write over the existing value, duration
            // clears existing timeout
            clearTimeout(get[2])
            this.data.set(key, [value, duration, ref])
            return true
        } else {
            // if key does not exist return false
            // store k:v:duration that auto deletes once duration is up
            this.data.set(key, [value, duration, ref])
            return false
        }
        // if key doesn't exist -> set key:value, timer
        // if key DOES exist -> write over the key value, add new timer
    }

    get(key: number): number {
        const res = this.data.get(key)
        return res ? res[0] : -1 
    }

    count(): number {
        // returns # of current unexpired keys
        return this.data.size
    }
}

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */