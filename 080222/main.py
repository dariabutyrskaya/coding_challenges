'''


Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.


https://leetcode.com/problems/permutations/


'''


def permute(nums):
    result = []
        
    #base case, if one value
    if len(nums) == 1:
    #only one permutation
        return [nums[:]]
        
    #go through every value in nums 
    for i in range(len(nums)):
        # take first value and pop it off
        n = nums.pop(0)
    
        perms = self.permute(nums)
            
        #go through each permutations, append and add them to the result
        for perm in perms:
            perm.append(n)
                
        result.extend(perms)
        #append at the back of the array the item back
        nums.append(n)

    return result