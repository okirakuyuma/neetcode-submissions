class Solution:

    def encode(self, strs: List[str]) -> str:
        str_with_num=""
        for s in strs:
            num=len(s)
            str_with_num+=str(num)+"#"+s
        return str_with_num
    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i<len(s):
            num=""
            while s[i].isdigit():
                num+=s[i]
                i+=1
            length=int(num)
            i+=1
            word=s[i:i+length]
            result.append(word)
            i+=length
        return result
                

