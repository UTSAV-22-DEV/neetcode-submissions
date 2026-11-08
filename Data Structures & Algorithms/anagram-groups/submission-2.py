
# 2. Character Count Array as Key Approach — Optimal for Long Strings

# • How it works: Instead of sorting, count the frequency of each character (from a to z) using a fixed-size array of 26 integers. Convert this count array into an immutable tuple to use as a hash map key. Words like "eat" and "tea" will both yield the exact same 26-element tuple representation.
# • Time Complexity: \(O(N \cdot K)\), since counting characters takes linear time proportional to the length of the string.
# • Space Complexity: \(O(N \cdot K)\) to store the map keys and values.
# • Best used when: The length of individual strings (K) is large, rendering the \(O(K \log K)\) sorting step inefficient.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map=defaultdict(list)
        for s in strs:
            count=[0]*26
            for char in s:
                count[ord(char)-ord('a')]+=1
            anagram_map[tuple(count)].append(s)
        return list(anagram_map.values())

        