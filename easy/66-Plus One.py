class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        done = False
        i = len(digits)-1
        while done == False:
            digits[i]+=1
            if digits[i]>9:
                digits[i]=0
                if i==0:
                    digits.insert(0,0)
                else:
                    i-=1
            else:
                done = True
        return digits
