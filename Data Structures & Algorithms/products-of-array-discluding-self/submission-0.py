class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product_list = []
        for i in range(len(nums)):

            pop_list = nums.copy()

            pop_list.pop(i)

            product=1
            for i in pop_list:
                product*=i
            product_list.append(product)
        
        return product_list