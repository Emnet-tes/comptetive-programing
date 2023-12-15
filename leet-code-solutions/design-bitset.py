class Bitset:

    def __init__(self, size: int):
       self.bitset=['0']*size
       self.keeper=['1']*size
       self.cnt=0      
    def fix(self, idx: int) -> None:
        if self.bitset[idx]=='0':
           self.bitset[idx]='1'
           self.cnt+=1
        self.keeper[idx]='0'
        

    def unfix(self, idx: int) -> None:
        if self.bitset[idx]=='1':
            self.bitset[idx]='0'
            self.cnt-=1
        self.keeper[idx]='1'
    def flip(self) -> None:
        self.bitset,self.keeper=self.keeper,self.bitset
        self.cnt=len(self.bitset)-self.cnt
    def all(self) -> bool:
        return self.cnt==len(self.bitset)
    def one(self) -> bool:
        return self.cnt

    def count(self) -> int:
        return self.cnt
        
    def toString(self) -> str:
       
        return ''.join(self.bitset)




# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()