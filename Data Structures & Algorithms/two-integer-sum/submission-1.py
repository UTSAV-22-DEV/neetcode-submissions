class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                if arr[i]+arr[j]==target:
                    return [i,j]
        return []

# Approach	Time Complexity	Space Complexity	
# Brute Force	\(O(n^2)\)	\(O(1)\)	No
