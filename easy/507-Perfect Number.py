class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = [1]
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                divisors.append(i)
                divisors.append(num/i)
        if num==1:
            return False
        return sum(divisors)==num