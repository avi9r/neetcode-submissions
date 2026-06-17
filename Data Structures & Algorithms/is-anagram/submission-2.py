class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr = sorted(list(s))
        t_arr = sorted(list(t))
        if s_arr == t_arr:
            return True
        else:
            return False