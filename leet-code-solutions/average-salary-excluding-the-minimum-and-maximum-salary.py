class Solution:
    def average(self, salary: List[int]) -> float:
        minval=min(salary)
        maxval=max(salary)
        sumval=sum(salary)-minval-maxval
        print(sumval)
        return sumval/(len(salary)-2)