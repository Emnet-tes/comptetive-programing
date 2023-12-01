class Solution:
    def interpret(self, command: str) -> str:
        n=command
        mylist=[]
        for i in range(len(n)):
            if n[i]=="G" :
                mylist.append("G")
            elif n[i]=="(" and n[i+1]==")":
                mylist.append("o")
            elif n[i]=="("and n[i+1]=="a":
                mylist.append("al")
        return "".join(mylist)