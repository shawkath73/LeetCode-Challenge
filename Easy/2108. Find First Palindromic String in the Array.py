class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            left_char,right_char = 0,len(word)-1
            while word[left_char] == word[right_char]:
                if left_char >= right_char:
                    return word
                left_char,right_char = left_char+1,right_char-1
        return ""
        '''for word in words:
            if word == word[::-1]:
                return word
        return "" '''   