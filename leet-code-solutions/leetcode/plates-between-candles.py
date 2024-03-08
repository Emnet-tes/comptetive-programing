class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # * plate | candle
        # to return the number of plates between candles
        size=len(s)
        left,right,ans,pre=[],[],[],[]
        
        postion=-1

        for i,n in enumerate(s):
            if n == '|':
                postion=i
            left.append(postion)
        cnt=0
        #right nearest candle
        for i,n in enumerate(s):
            
            if n == '|':
                cnt+=1
                while cnt:
                    right.append(i)
                    cnt-=1
            else:
                cnt+=1
        while cnt:
            if right:
                right.append(right[-1])
            else:
                right.append(-1)
            cnt-=1
        if s[-1] == '|':
            right[-1] = -1

        #prefix of the plates
        cnt=0
        for n in s:
            if n == '*':
                cnt+=1
            pre.append(cnt)
        
        for start,end in queries:
            
            left_candle= right[start]
            right_candle=left[end]
            
            if right_candle == left_candle or right_candle< left_candle or left_candle == -1 or right_candle == -1:
                ans.append(0)
            else:
                diff=pre[right_candle]-pre[left_candle]
                ans.append(diff)
            
        return ans
        

