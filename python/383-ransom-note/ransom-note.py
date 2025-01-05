from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = Counter(magazine)
        for elem in ransomNote:
            if m[elem] != 0:
                m[elem] -= 1
            else:
                return False
        return True
        