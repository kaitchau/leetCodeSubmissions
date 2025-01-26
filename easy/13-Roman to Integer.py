class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        string = list(s)
        skip = False
        ans = 0
        for i in range(len(s)-1,-1,-1):
            if skip == True:
                skip = False
                print("skipped")
                continue
            if string[i]=='I':
                ans+=1
            elif string[i] == 'V':
                ans+=5
                if i>0 and string[i-1]=='I':
                    ans-=1
                    skip = True
            elif string[i] == 'X':
                ans+=10
                if i>0 and string[i-1]=='I':
                    ans-=1
                    skip = True
            elif string[i] == 'L':
                ans+=50
                if i>0 and string[i-1]=='X':
                    ans-=10
                    skip=True
            elif string[i] == 'C':
                ans+=100
                if i>0 and string[i-1]=='X':
                    ans-=10
                    skip=True
            elif string[i] == 'D':
                ans+=500
                if i>0 and string[i-1]=='C':
                    ans-=100
                    skip=True
            elif string[i] == 'M':
                ans+=1000
                if i>0 and string[i-1]=='C':
                    ans-=100
                    skip=True
            print("i="+str(i)+",ans="+str(ans))

        return ans
            
#

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        string = list(s)
        ans = 0
        for i in range(len(s)-1,-1,-1):
            if i+1<len(s) and dict[string[i]]<dict[string[i+1]]:
                ans-=dict[string[i]]
                print("-i="+str(i)+",ans="+str(ans))
                continue
            ans+=dict[string[i]]
            print("+i="+str(i)+",ans="+str(ans))
        return ans