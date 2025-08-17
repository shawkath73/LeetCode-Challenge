class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        result = ""
        for word in words:
            result += word[0]
        return result == s    
                     