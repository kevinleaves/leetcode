class TimeMap:
    def __init__(self):
        self.obj = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key doesn't exist, create it w/ value being empty array
        self.obj[key] = self.obj.get(key, [])

        # push (value, timestamp) tuple to the array
        self.obj[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # get on an empty TimeMap => returns ''
        if len(self.obj) == 0:
            return ""

        # if key doesn't exist, return ''
        if key not in self.obj:
            return ""

        # if only 1 item, return value
        if len(self.obj[key]) == 1:
            return self.obj[key][0][0]

        # if array has more than 1 item, bsearch it for the correct value using timestamp
        l, r = 0, len(self.obj[key]) - 1
        values = self.obj[key]

        # update this with the largest timestamp as we bsearch
        maxBelowTimestamp = [0, ""]
        while l <= r:
            mid = l + (r - l) // 2
            # mid = (l + r) // 2
            # if values[mid][1] < timestamp:
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] > timestamp:
                r = mid - 1
            else:
                maxBelowTimestamp[0] = max(maxBelowTimestamp[0], values[mid][1])
                maxBelowTimestamp[1] = values[mid][0]
                l = mid + 1

        return maxBelowTimestamp[1]
        # if i haven't found the value at the given timestamp yet, i return the value at timestamp that's to the left of it


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
