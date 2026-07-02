class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for i in s:
            if i == "(" or i == "{" or i == "[" :
                a.append(i)
            else:
                if not a:
                    return False
                x = a.pop()
                if x == "(" and i != ")":
                    return False
                if x == "{" and i != "}":
                    return False
                if x == "[" and i != "]":
                    return False
        return len(a) == 0