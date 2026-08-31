class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        most_common = counter.most_common(k)

        result = []

        for num, _ in most_common:
            result.append(num)
        
        return result
            