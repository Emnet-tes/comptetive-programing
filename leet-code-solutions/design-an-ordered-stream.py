class OrderedStream:

    def __init__(self, n: int):
        self.stream=defaultdict(str)
        self.n=n-1
        self.ptr=0
    def insert(self, idKey: int, value: str) -> List[str]:
        result=[]
        if idKey-1==self.ptr:
            self.stream[self.ptr]=value
            while self.ptr<=self.n and self.stream[self.ptr]!='':
                result.append(self.stream[self.ptr])
                self.ptr+=1
        else:
            self.stream[idKey-1]=value
        return result

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)