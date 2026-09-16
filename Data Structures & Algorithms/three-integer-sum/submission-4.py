class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i, anchor in enumerate(nums):
            seen = set()
            for eachPos in range(i+1, len(nums)):
                value = -anchor - nums[eachPos]
                if value in seen:
                    triplet = [nums[i], value, nums[eachPos]]
                    triplet.sort()
                    if triplet not in result:
                        result.append(triplet)
                else:
                    seen.add(nums[eachPos])

        return result