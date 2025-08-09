class Solution:
    def numberOfMatches(self, n: int) -> int:
        total_matches = 0
        while n > 1:
            total_matches += n // 2
            n = (n+1) // 2
        return total_matches    