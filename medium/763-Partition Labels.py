class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        coords={}
        for i,c in enumerate(s):
            if c not in coords:
                coords[c]=[i,i]
            else:
                coords[c][1]=i
        l,r=coords[s[0]][0],coords[s[0]][1]
        n=len(coords)
        keys=list(coords.keys())
        print(coords)
        print(keys)
        res=[]
        if n<2:
            return [len(s)]
        for i in range(1,n):
            char=keys[i]
            if coords[char][1]<r and i==n-1:
                print('hello')
                res.append(r-l+1)
                l,r=coords[char][0],coords[char][1]
                res.append(r-l+1)
            elif coords[char][1]<r:
                print('hi')
                res.append(r-l+1)
                l,r=coords[char][0],coords[char][1]
            else:
                r=max(r,coords[char][1])
        return res