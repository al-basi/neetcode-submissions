class Solution:
    def __init__(self):
        self.spacer = "$"

    def encode(self, strs: List[str]) -> str:        
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + self.spacer + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != self.spacer:
                j += 1
            l = int(s[i:j])
            start = j + 1
            end = start + l
            decoded.append(s[start:end])
            i = end
        
        return decoded