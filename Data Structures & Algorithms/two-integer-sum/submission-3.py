class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, num in enumerate(nums):
            numberToFind = target - num
            if numberToFind in seen:
                return [seen[numberToFind], idx]
            seen[num] = idx

        return []