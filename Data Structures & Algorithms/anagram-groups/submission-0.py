
# 1. Character Sorting as Key Approach — Standard/Most Intuitive

# • How it works: Iterate through the array of strings. For each string, sort its characters alphabetically (e.g., "eat" becomes "aet"). Use this sorted string as a key in a hash map, and append the original string to a list mapped to that key.
# • Time Complexity: \(O(N \cdot K \log K)\), where N is the number of strings and K is the maximum length of a string in the list (due to sorting each string).
# • Space Complexity: \(O(N \cdot K)\) to store the strings in the hash map.
# • Best used when: String lengths (K) are relatively short, making sorting fast and code readability a priority
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map=defaultdict(list)
        for s in strs:
            sorted_key="".join(sorted(s))
            anagram_map[sorted_key].append(s)
        return list(anagram_map.values())

        