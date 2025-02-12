class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        #this is a set
        hashmap = {(x,y) for x,y in points}
        print(hashmap)
        n = len(points)
        min_area=inf
        for i in range(n):
            for j in range(i+1, n):
                x1,y1 = points[i]
                x2,y2 = points[j]
                if (x1,y2) in hashmap and (x2,y1) in hashmap:
                    if (x1,y1) != (x2,y2):
                        area = abs(y2-y1)*abs(x2-x1)
                        min_area = min(min_area,area)
        return min_area if min_area!=inf else 0
