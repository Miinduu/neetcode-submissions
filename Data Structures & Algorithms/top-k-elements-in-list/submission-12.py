class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            currentCount = counts.get(num, 0)
            counts[num] = currentCount + 1

        freq = []
        for key in counts:
            if counts[key] not in freq:
                freq.append(counts[key])
        freq.sort()

        mostFrequentCounts = freq[-k:]

        mostFrequentNumbers = []
        for i in range(len(mostFrequentCounts)):
            i = i + 1
            num = mostFrequentCounts[-i]
            for key in counts:
                if len(mostFrequentNumbers) == k:
                    return mostFrequentNumbers
                if counts[key] == num:
                    mostFrequentNumbers.append(key)

        return mostFrequentNumbers
