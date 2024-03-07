class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        all_t=defaultdict(int)
        window=defaultdict(int)
        
        for n in t:
            all_t[n]+=1
        
        cur,needed=0,len(all_t)
        ans,min_window = [-1,-1],float('inf')
        left=0

        for right in range(len(s)):
            window[s[right]] += 1

            if s[right] in all_t and window[s[right]] == all_t[s[right]]:
                cur+=1
            
            while cur == needed:
                if right-left+1 < min_window:
                    ans=[left,right]
                    min_window=right-left+1

                window[s[left]]-=1

                if s[left] in all_t and window[s[left]] < all_t[s[left]]:
                    cur-=1
                left+=1
        return s[ans[0]:ans[1]+1]
