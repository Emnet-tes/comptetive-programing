class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score=0
        stack=[0]
        for n in s:
            if n=='(':
                stack.append(0)
            else:
                top=stack.pop()
                score=max(1,2*top)
                stack[-1]+=score
        return stack.pop()

        