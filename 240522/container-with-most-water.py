'''
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints 
of the i-th line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

'''


def maxArea(height):

    result = 0
    #initializing pointers    
    left, right = 0, len(height) - 1
    #left pointer point on the last element on the left
    #right - last element to the right
    while left < right:
        area = (right - left) * min(height[right], height[left])
        result = max(result, area)
            
        if height[left] < height[right]:
            left += 1

        elif height[left] > height[right]:
            right -= 1

        else:
            left += 1

        return result

heights_1 = [12, 3, 22, 9, 7, 11, 10, 12]
heights_2 = [1, 1]

print("Max container size for [12, 3, 22, 9, 7, 11, 10, 12] is: " + str(maxArea(heights_1)))
#84
print("Max container size for [1, 1] is: " + str(maxArea(heights_2)))
#1