from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # create a hash map and for each string map list (chars) -> list (str)
        # frequencies are the same for hashmap so the arrays of fixed size will work as a key

        hashmap = defaultdict(list)
        for str in strs:
            arr = [0]*26
            for s in str:
                arr[ord(s)-ord('a')] += 1
            hashmap[tuple(arr)].append(str)

        return list(hashmap.values())

        