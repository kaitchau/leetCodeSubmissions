# two pointers O(n) time complexity O(1) space complexity
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        l,r=0,n-1
        while l<r:
            xsum=numbers[l]+numbers[r]
            if xsum==target:
                return[l+1,r+1]
            elif xsum<target:
                l+=1
            else:
                r-=1
        return