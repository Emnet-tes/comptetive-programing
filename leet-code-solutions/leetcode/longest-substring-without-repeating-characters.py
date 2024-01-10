class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        box=defaultdict(int)
        size=0
        for right in range(len(s)):
            box[s[right]]+=1
            while box[s[right]]>1:
                box[s[left]]-=1
                left+=1
            size=max(size,right-left+1)
        return size