# The backtracking algorithm is a problem-solving approach that tries out all the possible solutions and chooses the best or desired ones. 
# Generally, it is used to solve problems that have multiple solutions. The term backtracking suggests that for a given problem, if the current solution is not suitable, eliminate it and then backtrack to try other solutions.

# Generally, the time complexity of backtracking algorithm is exponential (0(kn)). In some cases, it is observed that its time complexity is factorial (0(N!)).

# https://www.tutorialspoint.com/data_structures_algorithms/dsa_backtracking_algorithm.htm#:~:text=The%20backtracking%20algorithm%20is%20a,the%20best%20or%20desired%20ones.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        def backtracking(i):
            if i >= len(nums):
                res.append(temp.copy())
                return
            temp.append(nums[i])
            backtracking(i+1)

            temp.pop()
            backtracking(i+1)
        backtracking(0)
        return res
