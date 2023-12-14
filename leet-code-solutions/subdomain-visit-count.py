class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        li={}
        for i in range(len(cpdomains)):
            visits,website=cpdomains[i].split()
            subdomain=website.split('.')
            for i in range(len(subdomain)):
                s='.'.join(subdomain[i::])
                if s in li.keys():
                    li[s]=str(int(li[s])+int(visits))
                else:
                    li[s]=visits
        ans=[]
        for y in li.keys():
            ans.append(li[y]+' '+y)
        return ans

        