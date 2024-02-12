class Solution:
    def numberOfWays(self, s: str) -> int:
        select=0
        office=restaurant=office_restaurant=restaurant_office=0
        for n in s:
            if n=='0':
                office+=1
                restaurant_office+=restaurant
                select+=office_restaurant
            else:
                restaurant+=1
                office_restaurant+=office
                select+=restaurant_office
        return select
        