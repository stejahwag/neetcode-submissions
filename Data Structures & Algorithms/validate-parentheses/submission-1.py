class Solution:
    def isValid(self, s: str) -> bool:
        
        CloseOpenMap = {"}":"{", "]":"[", ")":"("}
        validation = []
        for c in s:
            if c in CloseOpenMap:
                if validation and validation[-1]==CloseOpenMap[c]:
                    validation.pop()
                else:
                    return False
            else:
                validation.append(c)
        return True if not validation else False