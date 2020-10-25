
'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

'''

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        #Assuming intervals are already sorted 
        #line 11-21 will take O(n)
        pos = -1
        for i in range(0, len(intervals)):
            if intervals[i][0] > newInterval[0]:
                pos = i
                break
            else: 
                i = i+1
        if pos != -1:
            intervals.insert(pos,newInterval)
        else:
            intervals.append(newInterval)
            
        
        temp = list()
        for i in intervals:
            if not temp or temp[-1][-1] < i[0]:
                temp.append(i)
            else:
                temp[-1][-1] = max(temp[-1][-1], i[1])
        return temp
                
                
