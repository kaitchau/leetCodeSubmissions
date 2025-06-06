class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        store = {}
        store["2"]="abc"
        store["3"]="def"
        store["4"]="ghi"
        store["5"]="jkl"
        store["6"]="mno"
        store["7"]="pqrs"
        store["8"]="tuv"
        store["9"]="wxyz"

        res=[]
        if digits=="":
            return []

        def dfs(i,s):
            if len(s) == len(digits):
                res.append(s)
                return
            options=store[digits[i]]
            for c in options:
                s+=c
                dfs(i+1,s)
                s = s[:-1]
        dfs(0,"")
        return res