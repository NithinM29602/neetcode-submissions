class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # [-4, -1, -1, 0, 1, 2]
        result = []
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    value = [nums[i], nums[j], nums[k]]
                    if value not in result:
                        result.append(value)
                    j += 1
                    k -= 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1

        return result

        


        