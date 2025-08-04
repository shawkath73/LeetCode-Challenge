class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxx=0
        for sentence in sentences:
            sentence = sentence.split()
            maxx = max(maxx,len(sentence))
        return maxx              