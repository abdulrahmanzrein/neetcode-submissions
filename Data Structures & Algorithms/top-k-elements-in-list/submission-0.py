class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for n in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, frequency in count.items():
            freq[frequency].append(num)
        
        result = []

        for frequency in range(len(freq) - 1, 0 , -1):
            for num in freq[frequency]:
                result.append(num)

                if len(result) == k:
                    return result