from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topfrequent = Counter(nums).most_common(k)
        result = []

        for num, count in topfrequent:
            result.append(num)
        return result    