class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        skip = 0
        for x in range(len(arr)):
            found = False
            if skip>0:
                skip=skip-1
                continue
            for piece in pieces:
                if isinstance(piece, list):
                    try:
                        if piece.index(arr[x]) == 0:
                            for y in range(len(piece)):
                                if arr[x+y] == piece[y]:
                                    print(str(arr[x+y])+" = "+str(piece[y]))
                                else:
                                    return False
                            skip = len(piece)-1
                            found = True
                    except:
                        continue
            if found == False:
                return False
        return True