class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for e in s:
            if e in "[{(":
                stack.append(e)
            else:
                if not stack:
                    return False
                h=stack.pop()
            if e==']' and h!='[':
                return False
            elif e=='}' and h!='{':
                return False
            elif e==')' and h!='(':
                return False
        return not stack
