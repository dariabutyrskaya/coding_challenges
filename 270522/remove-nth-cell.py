'''

Given an integer array nums, return an array answer such that answer[i]
 is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 
'''

def product_except_self(nums):
    result = [1]*(len(nums)) #result array w dimenson of length of nums, initial value 1
    prefix = 1 

    #go trough every position in the input array
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
        
    postfix = 1

    #starting at the end of input array in this case    
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result



