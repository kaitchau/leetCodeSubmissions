class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        ans=[]
        for string in strs:
            s=''.join(sorted(string))
            if s in groups:
                groups[s].append(string)
            else:
                groups[s] = [string]
        for group in groups:
            ans.append(groups[group])
        return ans