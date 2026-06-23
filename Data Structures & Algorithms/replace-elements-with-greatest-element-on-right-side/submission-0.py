class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # max_element = 0
        # for i in range(len(arr)-1):
        #      arr[i]=max(arr[i+1:])
        # arr[-1]=-1
        # return arr

        # intial max = -1
        # reverse iteration 
        # new max = max(oldmax, arr[i])

        right_max = -1

        for i in range(len(arr)-1, -1, -1):
            new_max = max(right_max, arr[i])
            arr[i] = right_max
            right_max = new_max
        return arr
