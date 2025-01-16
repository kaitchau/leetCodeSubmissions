class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = filter(lambda y: y.isdigit(),list(s))
        digit_set = list(set(arr))
        digit_set.sort()
        print(digit_set)
        if len(digit_set)>=2:
            return int(digit_set[len(digit_set)-2])
        return -1
        