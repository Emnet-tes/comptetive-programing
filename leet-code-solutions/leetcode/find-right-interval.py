class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        k = len(intervals)
        ans=[-1]*len(intervals)
        start_index={}
        for i,n in enumerate(intervals):
            start_index[n[0]]=i
        sorted_intervals=sorted(intervals , key = lambda x : x[0])

        for i,n in enumerate(intervals):
            postion=bisect_left(sorted_intervals,[n[1],-float('inf')])

            if postion != k:
                ans[i]=start_index[sorted_intervals[postion][0]]
        return ans
        