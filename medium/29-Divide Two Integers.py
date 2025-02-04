class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend<0)is(divisor<0)
        if dividend<0:
            dividend=-dividend
        if divisor<0:
            divisor=-divisor
        arr_dividend = list(str(dividend))
        print(arr_dividend)
        divid=0
        quotient = ''
        for i in range(len(arr_dividend)):
            print(i)
            divid=int(str(divid)+str(arr_dividend[i]))
            print('dividend:'+str(divid))
            ct=0
            while divid>=divisor:
                divid-=divisor
                ct+=1
            quotient+=str(ct)
            print('quotient:'+str(quotient))
        quotient = int(quotient)
        if not positive:
            quotient=-quotient
        if quotient>2147483647:
            quotient=2147483647
        return quotient
