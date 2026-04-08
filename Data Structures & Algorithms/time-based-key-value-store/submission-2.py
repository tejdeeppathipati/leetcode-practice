class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        l, r = 0, len(values) - 1
        if len(values) == 0:
            return ""
        while l < r:
            m = (r - l)//2 + l
            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] > timestamp:
                r = m - 1
            else:
                if values[m + 1][1] > timestamp:
                    return values[m][0]
                l = m + 1
        if values[l][1] > timestamp:
            return ""
        return values[l][0]
            
