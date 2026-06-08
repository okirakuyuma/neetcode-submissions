class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnums=""
        n=0
        i=0
        while n <len(s):
            if s[n].isalnum():
                alnums+=s[n]
            n+=1
        alnums=alnums.upper()
        while i <len(alnums):
            if not alnums[i] == alnums[-i-1]:
                return False
            i+=1
        return True
            

