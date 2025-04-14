class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize!=0:
            return False
        c=Counter(hand)
        for num in sorted(c.keys()):
            ct=c[num]
            if ct>0:
                for i in range(num,num+groupSize):
                    c[i]-=ct
                    if c[i]<0:
                        return False
        return True