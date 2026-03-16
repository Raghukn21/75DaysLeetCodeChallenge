import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # A dictionary to group anagrams together
        anagram_map = collections.defaultdict(list)
        
        for word in strs:
            # Sort the word to use as the dictionary key
            # e.g., "eat", "tea", and "ate" all become "aet"
            sorted_word = tuple(sorted(word))
            anagram_map[sorted_word].append(word)
            
        return list(anagram_map.values())