class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        max_sum = 0
        first_sum = 0
        second_sum = 0
        for i in range(len(nums)):
            if i+firstLen <= len(nums):
                first_sum = sum(nums[i:i+firstLen])
                if i > secondLen:
                    for ii in range(i):
                        if ii+secondLen <= i:
                            # print("1first: "+str(nums[i:i+firstLen])+", second: "+str(nums[ii:ii+secondLen]))
                            second_sum = sum(nums[ii:ii+secondLen])
                            if first_sum+second_sum>max_sum:
                                max_sum=first_sum+second_sum
                        
                if (i+firstLen)+secondLen <= len(nums):
                    for ii in range((i+firstLen), len(nums)-secondLen+1):
                        if ii+secondLen<=len(nums):
                            # print("2first: "+str(nums[i:i+firstLen])+", second: "+str(nums[ii:ii+secondLen]))
                            second_sum = sum(nums[ii:ii+secondLen])
                            if first_sum+second_sum>max_sum:
                                max_sum=first_sum+second_sum
        return max_sum

