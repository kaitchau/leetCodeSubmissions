class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        res=0
        i,j=0,len(people)-1
        while i<=j:
            boat = limit - people[i]
            i+=1
            if i-1!=j and boat>=people[j]:
                j-=1
            res+=1
        return res
        