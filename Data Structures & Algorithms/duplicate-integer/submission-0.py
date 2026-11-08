class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n=len(nums)
        return any(nums[i]==nums[i+1] for i in range(0,n-1)) 