class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # add nums to stack and for each number check to see if new is larger
        # if new num is larger remove the top value from stack and account for the distance
        # for the stack it is a tuple with temp, and index

        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            temp = temperatures[i]
            
            while stack and stack[-1][0] < temp:
                index = stack[-1][1]
                stack.pop()
                res[index] = i - index 
            
            stack.append((temp, i))
        
        return res