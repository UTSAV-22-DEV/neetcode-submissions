class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        prev=0
        count=1
        maxcount=1
        if not nums:
            return 0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if nums[i]-nums[i-1]==1:
                prev=i
                count+=1
                maxcount=max(maxcount,count)
            else:
                count=1
        return maxcount

