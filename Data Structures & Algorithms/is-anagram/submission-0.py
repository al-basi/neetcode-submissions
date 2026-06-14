class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s: dict = {}
        chars_t: dict = {}

        self.add_to_dict(chars_s, s)
        self.add_to_dict(chars_t, t)

        return chars_s == chars_t

    def add_to_dict(self, chars_dict: dict, string: str) -> None:
        for char in string:
            if char in chars_dict:
                chars_dict[char] += 1
            else:
                chars_dict[char] = 1
        
