class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(arr):
            complement=target-num
            if complement in seen:
                return [seen[complement],i]
            seen[num]=i
        return []


# 2. Hash Map (One-Pass) Approach — Optimal for Unsorted Arrays

# • How it works: Traverse the array once. For each element num, calculate its complement (target - num). Check if the complement already exists in a hash map (dictionary). If it does, return its index and the current index. If not, store the current num and its index in the hash map.
# • Time Complexity: \(O(n)\) average case
# • Space Complexity: \(O(n)\) to store elements in the hash map
# • Best used when: Standard interview/LeetCode variation where you need the indices in a single pass