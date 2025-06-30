def gcd(a,b):
    return a if b == 0 else gcd(b,a%b)
class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return gcd(min(nums),max(nums))     