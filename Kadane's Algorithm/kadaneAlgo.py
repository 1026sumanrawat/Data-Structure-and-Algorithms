# https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
#  Maximum Subarry Problems

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        currSum = 0
        for num in nums:
            currSum += num
            maxi = max(currSum, maxi)
            if currSum < 0:
                currSum = 0
        return maxi
