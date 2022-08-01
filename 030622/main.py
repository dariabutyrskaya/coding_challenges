'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Constraints:
 - 1 <= intervals.length <= 104
 - intervals[i].length == 2
 - 0 <= starti <= endi <= 104

'''


def merge(intervals):
#sorting a list of pairs, sorting by the start value
    intervals.sort(key=lambda i: i[0])
    #merged intervals = first interval, to avoid edge case
    output = [intervals[0]]
    #iterate thru every single interval in sorted order
    for start, end in intervals[1:]:  # 1: because we got the first interval as a default
        lastEnd = output[-1][1]  # the end value of most recent added interval

        #if start value start or equal to last ending value, it means it overlapping
        if start <= lastEnd:
            #merge them then! (take the max ending value of itself)
            output[-1][1] = max(lastEnd, end)
        else:
            #not overlapping, but we still need to add the interval to the output
            output.append([start, end])
            
    return output