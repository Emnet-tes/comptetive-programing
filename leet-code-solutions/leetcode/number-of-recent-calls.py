class RecentCounter:

    def __init__(self):
        self.queue=[]

    def ping(self, t: int) -> int:
        self.queue.append(t)
        maxi=max(t,t-3000)
        mini=min(t,t-3000)
        cnt=0
        for n in self.queue:
            if n<mini or n>maxi:
                continue
            else:
                cnt+=1
        return cnt
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)