#brute force O(N^2) time complexity O(1) space complexity
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        max_area=0
        for i in range(n):
            for j in range(i+1,n):
                area = min(height[i],height[j])*(j-i)
                max_area=max(max_area,area)
        return max_area

# two pointer O(n) time complexity O(1) space complexity
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l,r = 0,n-1
        res=0
        while l<r:
            area = min(height[l],height[r])*(r-l)
            res=max(res,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res
