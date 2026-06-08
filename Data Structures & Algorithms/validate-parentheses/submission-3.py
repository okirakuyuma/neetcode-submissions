class Solution:
    def isValid(self, s: str) -> bool:
        characters = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack=[]
        for c in s:
            if c not in characters:
                stack.append(c)
            else:
                if not stack:
                    return False

                char=stack.pop()
                if not characters[c]==char:
                    return False
        return len(stack)==0


        
        