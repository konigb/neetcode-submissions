from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket_map = defaultdict(str)
        bracket_map['('] = ')'
        bracket_map['{'] = '}'
        bracket_map['['] = ']'

        for s_char in s:
            if stack and s_char in ['}', ']', ')']:
                candidate = stack[-1]
                stack.pop()
                if bracket_map[candidate] != s_char:
                    return False
            else:
                stack.append(s_char)
        
        return len(stack) == 0
