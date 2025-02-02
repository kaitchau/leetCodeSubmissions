class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res+=str(len(s))+'#'+s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        ans = []
        while i<len(s):
            length=''
            while s[i]!='#':
                length+=s[i]
                i+=1
            i+=1 # move past the #
            ilength=int(length)
            ans.append(s[i:(i+ilength)])
            i+=ilength
        return ans
