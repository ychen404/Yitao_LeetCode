class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        temp_sum = 0
        for i in range(len(nums)):
            temp_sum += nums[i]
            running_sum.append(temp_sum)
        
        print(running_sum)
        return running_sum