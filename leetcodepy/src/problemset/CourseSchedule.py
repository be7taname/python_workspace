'''
Created on Oct 11, 2015

@author: mianmianba
'''

class CanFinish(object):
    def solutions(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses == 1: return True
        srtedPrereq = [[] for x in range(numCourses)]
        for prereq in prerequisites:
            srtedPrereq[prereq[0]].append(prereq[1])
        visited = [False] * numCourses
        marked = [False] * numCourses
        for course in range(numCourses):
            if visited[course] == False:
                marked[course] = True
                if self.visitCourse(course, srtedPrereq, visited, marked) == False: return False
                else:
                    marked[course] = False
        return True
        
    def visitCourse(self, course, srtedPrereq, visited, marked):
        if srtedPrereq[course] == []: 
            visited[course] = True
            return True
        else:
            for precourse in srtedPrereq[course]:
                if visited[precourse] == True: continue
                elif marked[precourse] == True:
                    return False
                else:
                    marked[precourse] = True
                    if self.visitCourse(precourse, srtedPrereq, visited, marked) == False: 
                        return False
                    else: 
                        marked[precourse] = False
        visited[course] = True
        return True
    