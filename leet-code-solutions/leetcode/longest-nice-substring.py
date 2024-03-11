
class Solution:
    def longestNiceSubstring (self, s: str) -> str:

        n = len(s)

        mx = 0

        
        k = -1

        for i in range(len(s)):

            lower = 0

            upper = 0

            for j in range(i, n):

                c = s[j]

                if c.islower():

                    lower |= 1 << (ord(c) -ord('a'))

                else:

                    upper |= 1 << (ord(c) - ord('A'))

                if lower == upper and mx < j - i + 1:

                    mx = j - i + 1

                    k = i

        return "" if k == -1 else s[k:k+mx]

          