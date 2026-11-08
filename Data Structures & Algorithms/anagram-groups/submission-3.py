
# 3. Prime Factorization Product Approach — Mathematical Trick

# • How it works: Map each of the 26 English letters to a unique prime number (e.g., a->2, b->3, c->5, etc.). The key for a string is calculated by multiplying the prime values of all its characters. Because of the Fundamental Theorem of Arithmetic, every unique combination of characters will result in a unique product (e.g., "abc" and "cab" both equal 2 × 3 × 5 = 30).
# • Time Complexity: \(O(N \cdot K)\)
# • Space Complexity: \(O(N \cdot K)\)
# • Drawback & Limitations: In languages like Java or C++, calculating the product of a long string can easily lead to integer overflow. Python handles arbitrarily large integers automatically, but this approach remains bounded by performance bottlenecks when working with massive numbers.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101] 
        anagram_map=defaultdict(list)       
        for s in strs:
            product=1
            for char in s:
                product*=primes[ord(char)-ord('a')]
            anagram_map[product].append(s)
        return list(anagram_map.values())

        