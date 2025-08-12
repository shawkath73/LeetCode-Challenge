class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = 0
        rightSum = sum(nums)
        answer = [0] * len(nums)
        for i in range(len(nums)):
            leftSum += nums[i-1] if i > 0 else 0
            rightSum -= nums[i]
            answer[i] = abs(leftSum - rightSum)
        return answer       