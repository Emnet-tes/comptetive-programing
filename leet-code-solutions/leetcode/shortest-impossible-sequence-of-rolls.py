class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        cnt=0
        roll=set()
        for n in rolls:
            roll.add(n)
            if len(roll)==k:
                cnt+=1
                roll.clear()

        return cnt+1
