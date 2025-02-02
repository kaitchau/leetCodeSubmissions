class Solution:
    def mySqrt(self, x: int) -> int:
        s = str(x)
        divisor = 0
        quotient = ''
        mult = 0
        fit = 0
        if len(s)%2==1:
            s = '0'+s
        dividend = int(s[:2])
        print(s)
        for i in range(0,len(s),2):
            if i!=0:
                dividend = dividend*100+int(s[i:i+2])
            print("i:"+str(i)+",dividend:"+str(dividend))
            divisor = 1
            fit=0
            print(str(mult)+str(divisor))
            while int(str(mult)+str(divisor))*divisor<=dividend:
                print(str(mult)+str(divisor))
                fit = divisor
                divisor+=1
            dividend -= int(str(mult)+str(fit))*fit
            print("d*d:"+str(fit*fit))
            print("divisor:"+str(fit)+",dividend:"+str(dividend))
            quotient += str(fit)
            mult = int(quotient)*2
        print("quotient:"+quotient)
        return int(quotient)