class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left=0
        right=len(skill)-1
        target=skill[0]+skill[right]
        ans=0
        while left<right:
            if skill[left]+skill[right]==target:
                ans+=skill[left]*skill[right]
                left+=1
                right-=1
            else:
                return -1
        return ans