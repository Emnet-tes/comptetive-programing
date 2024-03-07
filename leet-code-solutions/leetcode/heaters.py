class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        maxi=0
        heaters.sort()
        for i in range(len(houses)):

            left = 0
            right = len(heaters)-1
            mini=float('inf')

            while left < right :

                mid = (left+right)//2

                if heaters[mid] == houses[i]:
                    mini=0
                    break

                elif heaters[mid] < houses[i]:
                    mini = min(mini,abs(heaters[mid] - houses [i]))
                    left= mid+1

                else:
                    mini = min(mini,abs(heaters[mid] - houses [i]))
                    right = mid
            
            mini=min(mini,abs(heaters[left] - houses [i]))
            maxi=max(maxi,mini)
        return maxi