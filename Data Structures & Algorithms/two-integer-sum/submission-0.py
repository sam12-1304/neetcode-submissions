class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}
        for i, current_num in enumerate(nums):
            needed_num = target - current_num
            if needed_num in prev_map:
                return [prev_map[needed_num],i]
            prev_map[current_num] = i
        return []        