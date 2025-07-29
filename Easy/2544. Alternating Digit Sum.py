class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        total = 0
        for i in range(0,len(n)):
            total += (-1) ** i * int(n[i])
        return total    