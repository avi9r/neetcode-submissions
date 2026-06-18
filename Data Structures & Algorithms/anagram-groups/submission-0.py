class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        for item in strs:
            anagrams = [x for x in strs if sorted(list(x))==sorted(list(item))]
            if anagrams not in res:
                res.append(anagrams) 
            
        return res