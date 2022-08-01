'''

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Constraints:
 - 1 <= intervals.length <= 10^5
 - intervals[i].length == 2
 - -5 * 10^4 <= starti < endi <= 5 * 10^4
 
 
'''


def no_overlap(intervals):
    #sort the list of intervals based on entire pair
    intervals.sort()
    res = 0
    #first end value
    prevEnd = intervals[0][1]
    # iterate thru remaining intervals, start at index 1
    for start, end in intervals[1:]:
        #nin overlaping if start value more or equal than prev value
        if start >= prevEnd:
            #new end value
            prevEnd = end
        else:
            #if they r ovelapping, remove one of the intervals
            res += 1
            #update prevEnd w the smallest end value
            prevEnd = min(end, prevEnd)
            
    return res