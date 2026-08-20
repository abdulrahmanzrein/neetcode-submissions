class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #store elements we seen before that are not needed

        for i, num in enumerate(nums): #gives us the index and the number so we can store it as "weve seen that number before"
            needed = target - num #the num needed to get the target after seeing one element

            if needed in seen: 
                return[seen[needed], i]
            
            seen[num] = i #store the number and its index so we can later look it up

