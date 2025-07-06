class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add=0
        prod=1
        while n > 0:
            add += n%10
            prod *= n%10
            n //= 10
        return prod-add     