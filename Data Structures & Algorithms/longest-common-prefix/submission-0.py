class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        from os.path import commonprefix
        return commonprefix(strs)
        