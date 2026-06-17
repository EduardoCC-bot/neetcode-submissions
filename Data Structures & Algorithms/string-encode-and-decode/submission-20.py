class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for s in strs:
            encode = encode + str(len(s)) + "#" + s

        print(encode)
        return encode

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            j = i
            while(s[j] != "#"):
                j+=1
            tam = int(s[i:j])
            i = j+1
            j = i + tam

            res.append(s[i:j])
            i=j

        return res
                



