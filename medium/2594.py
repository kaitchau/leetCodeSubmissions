class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l,r=1, max(ranks)*(cars**2)
        res=0
        while l<=r:
            m=l+(r-l)//2
            ct=0
            for rank in ranks:
                ct+=(m//rank)**2
            print(ct)
            if ct<cars:
                l=m+1
            else:
                r=m-1
                print('hi')
                res=min(res,m)
        return r