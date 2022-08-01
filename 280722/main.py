'''

Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing
the order of the remaining elements. 

For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104

'''


def subseq(nums):

    cach = [1] * len(nums) #cache, initially set to one
    # Interate through every index in the reange of input array, in reverse order
    for i in range(len(nums) - 1, -1, -1):
        # iterate through every subsequence that came after it
        for j in range(i + 1, len(nums)):
            # check if value at i is less than value in j, then update the longest subsequence 
            if nums[i] < nums[j]:
                cach[i] = max(cach[i], 1 + cach[j])

    return max(cach) 


if __name__ == '__main__':
    pass
