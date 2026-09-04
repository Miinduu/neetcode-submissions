class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string = encoded_string + string
            encoded_string = encoded_string + "€€"

        return encoded_string

    def decode(self, s: str) -> List[str]:
        print(f"string to decode: {s}")
        word = ""
        decoded_strs = []
        
        i = 0
        while i < len(s):
            flag = s[i] + s[i + 1]
            if flag == '€€':
                decoded_strs.append(word)
                word = ""
                i = i + 2
            else:
                word = word + s[i]
                i = i + 1
            
        return decoded_strs
