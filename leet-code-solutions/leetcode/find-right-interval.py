class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        size = len(intervals)
        start_idx = defaultdict(int)
        for i,n in enumerate(intervals):
            start_idx[n[0]] = i
        sorted_intervals=sorted(intervals , key = lambda x : x[0])
        ans = [-1]*size
        for i,n in enumerate(intervals):
            postion = bisect_left(sorted_intervals,[n[1],float('-inf')])
            if postion != size:
                ans[i]=start_idx[sorted_intervals[postion][0]]
        return ans