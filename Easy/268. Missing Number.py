class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        sum = (n * (n+1)) // 2
        for num in nums:
            res+=num
        return sum-res      