class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        store1= defaultdict(int)
        store2 = defaultdict(int)
        n=len(nums1)
        n2=len(nums2)
        res = 0
        for i in range(n):
            store1[nums1[i]*nums1[i]]+=1
        for i in range(n2):
            store2[nums2[i]*nums2[i]]+=1
        for j in range(n2):
            for k in range(j+1,n2):
                product=nums2[j]*nums2[k]
                if product in store1:
                    res+=store1[product]
        for j in range(n):
            for k in range(j+1,n):
                product=nums1[j]*nums1[k]
                if product in store2:
                    res+=store2[product]
        return res
