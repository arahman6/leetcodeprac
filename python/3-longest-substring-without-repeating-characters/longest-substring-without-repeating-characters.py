class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        sub_set = set()

        for r in range(len(s)):
            while s[r] in sub_set:
                sub_set.remove(s[l])
                print('remove', r, s[l])
                l += 1
            
            sub_set.add(s[r])
            max_len = max(max_len, r - l + 1)
            print('add', r, s[r], max_len)
        
        return max_len
        