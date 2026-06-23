class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
                
        tracker = set()

        for n in nums:
            if n in tracker:
                return True
            else:
                tracker.add(n)
        return False


        # for i in nums:
        #     count=0
        #     for j in nums:
        #         if i==j:
        #             count+=1
        #         if count>=2:
        #             return True
        # return False

        
            
