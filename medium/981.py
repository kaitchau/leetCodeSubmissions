class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]
        l,r=0,len(arr)-1
        res = ''
        while l<=r:
            m=l+(r-l)//2
            time=arr[m][1]
            val=arr[m][0]
            res=val
            if time==timestamp:
                break
            elif time>timestamp:
                r=m-1
            else:
                l=m+1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)