class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair_list = []
        for i in range(len(position)):
            pair_list.append((position[i], speed[i]))

        pair_list.sort(reverse=True)
        stack = []

        for p,s in pair_list:
            time = (target - p)/s
            stack.append(time)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        