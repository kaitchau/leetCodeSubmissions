class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        cells=defaultdict(list) #distance, cell
        res=[]
        for r in range(rows):
            for c in range(cols):
                dist = abs(r-rCenter)+abs(c-cCenter)
                cells[dist].append((r,c))
        dists=list(cells.keys())
        dists.sort()
        for dist in dists:
            res+=cells[dist]
        return res
        