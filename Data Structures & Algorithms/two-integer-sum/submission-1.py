class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = []
        # Loop through all of the numbers
        for idx, num in enumerate(nums):
        # subtract to find number we are looking for to get correct result
            numberToLookFor = target - num
        # Check if that number is in the seen set
            if numberToLookFor in seen:
        # if yes return index of that number
                for idx2, num2 in enumerate(nums):
                    if idx == idx2:
                        continue
                    if num2 == numberToLookFor:
                        return [idx2, idx]

            seen.append(num)


        return []      


