'''
Given a string s, find the length of the longest substring without repeating characters.

Constraints:
 - 0 <= s.length <= 5 * 10*4
 - s consists of English letters, digits, symbols and spaces.

'''


def longest_no_repeat(s):
    charSet = set() #character set
    
    left = 0 #left pointer
    result = 0 
        
    for right in range(len(s)): #right pointer in for loop thru every single character
        while s[right] in charSet: #if duplicate 
            charSet.remove(s[left]) #remove left charater from the set
            left += 1 #update left pointer 
        charSet.add(s[right]) #right to the character set add
        result = max(result, right - left + 1) #update result as max 

    return result

if __name__ == '__main__':
    pass
