class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        size=0
        left=0
        box=defaultdict(int)
        most_frequent = 0
        for right in range(len(s)):
            box[s[right]]+=1
            most_frequent = max(most_frequent, box[s[right]])
            if (right-left+1)-most_frequent>k:
                box[s[left]]-=1
                left+=1
            size=max(size,right-left+1)
        return size