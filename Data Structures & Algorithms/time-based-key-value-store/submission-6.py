class TimeMap:
    def __init__(self):
        self.timeset = defaultdict(list)
        # or self.timeset = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key not in self.timeset:
        #     self.timeset[key] = []
        #     self.timeset[key].append([value, timestamp])
        # else:
        #     self.timeset[key].append([value, timestamp])
        self.timeset[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        val = self.timeset.get(key)
        cur = ""
        if not val:
            return ''

        left,right = 0, len(val) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if timestamp < val[mid][1]:
                right = mid - 1
            elif timestamp > val[mid][1]:
                cur = val[mid][0]
                left = mid + 1
            elif timestamp == val[mid][1]:
                return val[mid][0]
        return cur
                

                

