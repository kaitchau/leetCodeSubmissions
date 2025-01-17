#O(N)
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        least_index_sum = 9999
        ans = []
        for i in range(len(list1)):
            try:
                i2 = list2.index(list1[i])
                index_sum = i+i2
                if index_sum <= least_index_sum:
                    if index_sum<least_index_sum:
                        ans=[]
                    least_index_sum = index_sum
                    ans.append(list1[i])
            except:
                continue
        return ans