from collections import defaultdict
class TimeMap:
    # i need to perform binary search on the get, if the value is not present then return the value at the end
    def __init__(self):
        self.hashmap = defaultdict(list)
        # Need a hashmap : str - > array of tuples (str, int)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # Here we will berform a binary search
        # If we find a prev_timestamp == timestamp return 
        # If no such value is found the return the value at the end of the array
        if key not in self.hashmap:
            return ""

        l = 0
        r = len(self.hashmap[key]) - 1

        m = 0
        res = ""
        while l <= r:
            m = (l + r)//2

            if self.hashmap[key][m][1] <= timestamp:
                res = self.hashmap[key][m][0]
                l = m + 1
            elif self.hashmap[key][m][1] > timestamp:
                r = m - 1
        return res
        # res = ""
        # while m < len(self.hashmap[key]) and self.hashmap[key][m][1] < timestamp:
        #     res = self.hashmap[key][m][0]
        #     m += 1
        # while m >= 0 and m < len(self.hashmap[key]):
        #     if self.hashmap[key][m][1] < timestamp:
        #         res = self.hashmap[key][m][0]
        #         break
        #     m -= 1
        # return res 
