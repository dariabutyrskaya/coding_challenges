'''
You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Constraints:

 - 1 <= s.length <= 105
 - s consists of only uppercase English letters.
 - 0 <= k <= s.length

'''


def characterReplacement(s, k):
    count = {} #hasmap to count occurences
        
    res = 0 #the longest substring
    left = 0 #pointer
    for right in range(len(s)): #right pointer
        count[s[right]] = 1 + count.get(s[right],0) #for every character in position right increment count of it
        while (right - left + 1) - max(count.values()) > k: #check if window is not valid
            count[s[left]] -= 1 #decrement count of the character 
            left += 1
        res = max(res, right - left + 1) #max ever been (size of the window)
    return res
        

if __name__ == '__main__':
    pass
