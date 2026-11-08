

# 2. Bucket Sort Approach — Strictly Linear Time

# • How it works: Create an array of lists called buckets, where the index represents the frequency (the maximum possible frequency is n). Populate the buckets by placing each number into the list at index = its frequency. Finally, iterate through the buckets from the highest index (most frequent) down to 0, collecting elements until you have gathered k items.
# • Time Complexity: O(n), because you iterate through the input array, the unique keys, and the buckets array of size n exactly once.
# • Space Complexity: O(n) to store the frequency map and the bucket array.
# • Best used when: You need a guaranteed linear time complexity and memory overhead isn't an issue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        count=Counter(nums)
        buckets=[[] for _ in range(len(nums)+1)]
        for num,freq in count.items():
            buckets[freq].append(num)
        result=[]

        for i in range(len(buckets)-1,-1,-1):
            for num in buckets[i]:
                result.append(num)
                if len(result)==k:
                    return result