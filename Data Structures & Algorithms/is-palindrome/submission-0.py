class Solution:
    def isPalindrome(self, s: str) -> bool:
        st="".join(c for c in s if c.isalnum()).lower()
        l=0
        r=len(st)-1
        while l<r:
            if(st[l]!=st[r]):
                return False
            else:
                l+=1
                r-=1
        return True
        