class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = dict()
        for str in strs:
            if self.wordCountKey(str) not in a.keys():
                a[self.wordCountKey(str)] = []
            a[self.wordCountKey(str)].append(str)
        return list(a.values())        


    def wordCount(self, s: str) -> dict:
        a = dict()
        for c in [*s]:
            if c in a.keys():
                a.update({c: a.get(c) + 1})
            else:
                a.update({c: 1})
        return a

    def wordCountKey(self, s: str) -> str:
        a = str(sorted(self.wordCount(s).items()))
        return a