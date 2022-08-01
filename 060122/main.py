'''

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Constraints:
 - 1 <= nums.length <= 105
 - k is in the range [1, the number of unique elements in the array].
 - It is guaranteed that the answer is unique.

'''


#Bucket sort!
def topKFrequent(nums, k):
    #hashmap
    count = {}
    #empty array size of input+1
    frequency = [[] for i in range(len(nums)+1)]

    #go thru every value in nums and counts it occurence
    for n in nums:
        count[n] = 1 + count.get(n, 0)
        
    #goin thru each value we counted, in freq array append value n times
    for n, c in count.items():
        frequency[c].append(n)

    res = []
    
    #in decending value iterating *because we need top K
    for i in range(len(frequency) -1, 0, -1):
        #gettin top k values
        for n in frequency[i]:
            res.append(n)
            if len(res) == k:
                return res