class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        work_hash = dict()

        if len(pattern) != len(words): 
            return False
        if len(set(pattern)) != len(set(words)): 
            return False

        for i in range(len(words)):
            if words[i] not in work_hash: 
                work_hash[words[i]] = pattern[i]
            elif work_hash[words[i]] != pattern[i]: 
                return False
        return True
        