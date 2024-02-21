class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans=0
        rabits=Counter(answers)

        for n in rabits.keys():

            x = math.ceil(rabits[n]/(n+1))
            ans += (x*(n+1))
            
        return ans