class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        esum=sum(nums)
        dsum=0
        for i in range(0,len(nums)):
            while nums[i]>0:
                dsum+=nums[i]%10
                nums[i]//=10
        return abs(esum-dsum)