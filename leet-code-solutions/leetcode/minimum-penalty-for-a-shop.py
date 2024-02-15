class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ans,Diff = 0, 0
            
        for i in range(0, len(customers)):
            if customers[i] == 'Y':
                Diff -= 1
            else:
                Diff += 1
            
            if Diff < 0:
                Diff = 0;
                ans = i + 1;
        return ans;