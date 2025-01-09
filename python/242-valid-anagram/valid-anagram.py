class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = self.wordCount(s)
        t_dict = self.wordCount(t)
        if s_dict == t_dict:
            return True
        return False

    def wordCount(self, s: str) -> dict:
        a = dict()
        for c in [*s]:
            if c in a.keys():
                a.update({c: a.get(c) + 1})
            else:
                a.update({c: 1})
        return a