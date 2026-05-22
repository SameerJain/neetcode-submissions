class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        q = sorted(s)
        w = sorted(t)

        if q == w:
            return True

        return False