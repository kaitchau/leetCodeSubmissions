class Solution:
    def reorganizeString(self, s: str) -> str:
        ch_ct = Counter(s)
        print(ch_ct)
        #-freq to make the default minheap into a maxheap
        maxheap = [(-freq,c) for c,freq in ch_ct.items()]
        heapq.heapify(maxheap)
        res=''
        prevfreq,prevc=0,''
        while maxheap:
            freq,c = heapq.heappop(maxheap)
            if prevfreq<0:
                res+=prevc
                prevfreq+=1
                heapq.heappush(maxheap,(prevfreq,prevc))
            if c is not prevc:
                prevfreq,prevc = freq,c
        return res if len(res)==len(s) else ''