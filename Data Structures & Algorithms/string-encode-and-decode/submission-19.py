class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            stringLength = len(string)
            if stringLength < 10:
                stringLength = "00" + str(stringLength)
            elif stringLength < 100:
                stringLength = "0" + str(stringLength)
            else:
                stringLength = str(stringLength)
            encoded_string = encoded_string + stringLength + string

        return encoded_string

    def decode(self, s: str) -> List[str]:
        print(f"string to decode: {s}")
        word = ""
        decoded_strs = []
        
        i = 0
        stringLen = len(s)
        print("length of the string: ", stringLen)
        while i < stringLen:
            amountToWrite = int(s[i] + s[i+1] + s[i+2])
            if amountToWrite == 0:
                print("amount is 0")
                decoded_strs.append("")
            else:
                print("amount to write: ", amountToWrite)
                print("first letter", i + 3)
                print("last letter", i + amountToWrite + 3)
                word = s[i + 3:i + amountToWrite + 3]
                print("word: ", word)
                decoded_strs.append(word)
            i = i + amountToWrite + 3
            print("while loop ran")
            
        print(decoded_strs)
        return decoded_strs
