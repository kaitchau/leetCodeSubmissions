#time limit exceeded
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=[1]*n
        for i in range(n):   
            if i!=0:
                answer[i]*= reduce(operator.mul, nums[0:i])
            if i!=n-1:
                answer[i]*=reduce(operator.mul, nums[i+1:n+1])
        return answer

#O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=[1]*n
        prefix=[nums[0]]
        suffix=[1]*n
        suffix[n-1]=nums[n-1]
        for i in range(1,n):
            prefix.append(nums[i]*prefix[i-1])
        for i in range(n-2,-1,-1):
            suffix[i]=nums[i]*suffix[i+1]
        for i in range(n):
            if i==0:
                answer[i]=suffix[i+1]
            elif i==n-1:
                answer[i]=prefix[i-1]
            else:
                answer[i]=prefix[i-1]*suffix[i+1]
        return answer

# faster O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=[1]*n
        prefix=1
        for i in range(n):
            answer[i]*=prefix
            prefix*=nums[i]
        suffix=1
        for j in range(n-1,-1,-1):
            answer[j]*=suffix
            suffix*=nums[j]
        return answer