
# 1. Min-Heap (Priority Queue) Approach — The Standard Interview Fix

# • How it works: First, build the frequency map. Then, iterate through the unique elements and push them into a min-heap based on their frequency. If the size of the heap exceeds k, pop the least frequent element. By the end, the heap will contain exactly the top k most frequent elements.
# • Time Complexity: \(O(n \log k)\), because maintaining a heap of size k takes \(O(\log k)\) time for each of the elements.
# • Space Complexity: O(n) to store the elements in the frequency map.
# • Best used when: k is significantly smaller than the number of unique elements (\(k \ll n\)), making \(\log k\) negligible.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        freq=Counter(nums)
        for num,count in freq.items():
            heapq.heappush(heap,(count,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for count,num in heap]