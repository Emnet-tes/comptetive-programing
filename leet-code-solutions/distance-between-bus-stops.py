class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start<destination:
            clockwise=sum(distance[start:destination])
        else:
            clockwise=sum(distance[destination:start])
        total=sum(distance)
        print(clockwise)
        anticlockwise=total-clockwise
        
        return min(clockwise,anticlockwise)
        