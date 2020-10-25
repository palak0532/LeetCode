Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

 

Constraints:

    intervals[i][0] <= intervals[i][1]




class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #this sorting will take nlog(n) time that is by deafult for sorting functions
        intervals.sort(key = lambda x : x[0])
        print(intervals)
        temp = list()
        for interval in intervals:
            
            #If temp is empty or temp arrays last elements 1st position from last eg 
            #temp = [[1,5], [6,8]] then temp [-1] = [6,8] and temp[-1][-1] = 8  
            if not temp or temp[-1][-1] < interval[0]:
                temp.append(interval)
            else:
                temp[-1][-1] = max(temp[-1][-1] , interval[1])
        print(temp)
        return temp
                
                
           
        
