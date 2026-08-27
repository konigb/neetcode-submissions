class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create a hashmap

        # iterate over list

        # for each value in list call sorted() and map the sorted string to the word in list (append to end of list)

        # iterate over the keys,values in hashmap and return a list of lists

        hashmap = dict()

        for s in strs:

            sorted_s = ''.join(sorted(s))

            if hashmap.get(sorted_s) == None:
                hashmap[sorted_s] = [s]
            else:
                hashmap[sorted_s].append(s)
        
        res = []

        for k,v in hashmap.items():
            res.append(v)

        return res

