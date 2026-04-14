class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, v in enumerate(nums):
            hash[v] = i
        for i, v in enumerate(nums):
            if target - v in hash and hash[target - v] != i:
                return [i, hash[target - v]]