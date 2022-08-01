'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
 - [4,5,6,7,0,1,2] if it was rotated 4 times.
 - [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time
'''


def findmin(nums):
    res = nums[0] #random default value
    left, right = 0, len(nums) - 1 #pointers
        
    while (left <= right): #running binary search while pointer are in valid position
        if nums[left] < nums[right]: #if sorted
            res = min(res, nums[left]) #update result min
            break
        #if not sorted
        middle = (left + right) // 2 #computer mid point
        res = min(res, nums[middle]) # update result min
        if nums[middle] >= nums[left]: #are we gonna search to the left or to the right?
            left = middle + 1 #search right portion
        else: 
            right = middle - 1 #search left portion
    #until solution of searched array
    return res
        

if __name__ == '__main__':
    pass
