class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s = sorted(s)
        t = sorted(t)

        for idx, letter in enumerate(s):
            if letter == t[idx]:
                continue
            else:
                return False

        return True
        