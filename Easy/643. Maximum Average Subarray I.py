class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = 0
        n = len(nums)
        current_sum = sum(nums[:k])
        maxx_avg = current_sum / k
        for i in range(k,n):
            current_sum += nums[i] - nums[i-k]
            avg = current_sum / k
            maxx_avg = max (maxx_avg,avg)
        return maxx_avg