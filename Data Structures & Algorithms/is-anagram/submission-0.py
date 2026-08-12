class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        t_d = {}

        for i in range(len(s)):
            if s[i] not in s_d:
                s_d[s[i]] = 1
            else:
                s_d[s[i]]+= 1
        
        for j in range(len(t)):
            if t[j] not in t_d:
                t_d[t[j]] = 1
            else:
                t_d[t[j]]+= 1
        
        return s_d == t_d