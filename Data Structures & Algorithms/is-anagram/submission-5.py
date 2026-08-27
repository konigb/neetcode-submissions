class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len of s and t not equal exit (False)
        if len(s) != len(t):
            return False
        # create a map
        letter_map = dict()
        # iterate over s 
        for letter in s:
            # map each letter to frequency
            if letter_map.get(letter) == None:
                letter_map[letter] = 1
            else:
                letter_map[letter] += 1

        # iterate over t
        for letter in t:
            # if letter not in map exit (False)
            if letter_map.get(letter) == None:
                return False
            # reduce by 1
            letter_map[letter] -= 1
            # if frequency value is neg exit (False)
            if letter_map[letter] < 0:
                return False
        return True
        
        # return True
        