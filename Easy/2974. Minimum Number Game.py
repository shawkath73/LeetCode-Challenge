class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []
        for i in range(0,len(nums),2):
            fval=nums[i]
            sval=nums[i+1] 
            arr.append(sval)
            arr.append(fval)
        return arr     

        
        