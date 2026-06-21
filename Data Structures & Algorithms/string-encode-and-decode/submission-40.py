class Solution:

    def encode(self, strs: List[str]) -> str:        
        encode = ""
        for s in strs:
            encode = encode + str(len(s))
            encode = encode + "#"
            encode = encode + s
        return encode

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            print(i)
            tam = ''
            while s[i] != '#':
                tam = tam + s[i]
                i+=1
            i+=1
            res.append(s[i: i + int(tam)])
            i = i + int(tam)
        return res


