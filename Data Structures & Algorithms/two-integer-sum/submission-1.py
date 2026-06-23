class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # result = []
        # for i in range(len(nums)):
            
        #     for j in range(i+1, len(nums)):
                
        #         if nums[i]+nums[j]==target:
        #             result.append(i)
        #             result.append(j)
        # return result

        #############
        prev_map = {}

        for i, n in enumerate(nums):

            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i] 
            prev_map[n] = i