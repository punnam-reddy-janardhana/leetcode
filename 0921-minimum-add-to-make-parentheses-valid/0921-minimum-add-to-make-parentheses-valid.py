class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        x = []
        for i in s:
            if i =="(" :
                x.append(i)
            else:
                if not x:
                    x.append(i)
                    continue
                b =x[-1]
                if i ==")" and b =="(":
                    x.pop()
                else:
                    x.append(i)
        return len(x)



        