class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        for word in strs:
            sorted_key = "".join(sorted(word))
            word_dict.setdefault(sorted_key, []).append(word)
        return list(word_dict.values())    