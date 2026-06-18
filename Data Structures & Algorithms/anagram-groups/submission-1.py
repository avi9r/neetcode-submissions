class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        for item in strs:
            anagrams = [x for x in strs if sorted(x)==sorted(item)]
            if anagrams not in res:
                res.append(anagrams) 
            
        return res