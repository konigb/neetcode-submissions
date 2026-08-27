class Solution:

    def encode(self, strs: List[str]) -> str:
        # determine the length of each string and put the value in the form of 3 digits infront of each string
        # do this for all strings in list and combine to one word 
        # return value
        encoded_str = ""

        for s in strs:
            length = len(s)
            if length < 10:
                str_length = "00" + str(length)
            elif length < 100:
                str_length = '0' + str(length)
            else:
                str_length = str(length)
            encoded_str += str_length+s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # make a list
        # get the first 3 values as a substring
        # convert to a number
        # move index in for loop by 3 & get substring based on length
        # add extracted word to list
        # have step move the index by the length of word up till end of string
        #
        decoded_str = []
        idx = 0
        while idx < len(s):
            length = int(s[idx:idx+3]) # length of str
            idx += 3 # move index to start of str
            sub_str = s[idx:idx+length] # get the sub string
            decoded_str.append(sub_str) # append to list
            idx += length # change step dynamically so index is at next num
        return decoded_str
                
