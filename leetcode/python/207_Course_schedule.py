"""
    207. Course Schedule

    There are a total of n courses you have to take, labeled from 0 to n - 1.

    Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

    Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

    For example:

    2, [[1,0]]
    There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

    2, [[1,0],[0,1]]
    There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(prerequisites) == 0:
            return True

        if len(prerequisites) > numCourses*(numCourses-1) /2:
            return False

        courseDict = {}

        for pre in prerequisites:
            if pre[0] not in courseDict:
                courseDict[pre[0]] = [[pre[1],"unvisited"]]
            else:
                courseDict[pre[0]].append([pre[1],"unvisited"])

        if len(courseDict)==numCourses:
            return False


        for k , vs in courseDict.iteritems():
            res = self.helper(k,{k:1},courseDict)
            if res == False:
                return res

        return res

    def helper(self,key,dic,courseDict):

        for i ,v in enumerate(courseDict[key]):

            if v[0] in courseDict and v[1] == "unvisited":
                if v[0] in dic:

                    return False
                dic[v[0]] = 1
                courseDict[key][i] = [v[0],"visited"]
                res = self.helper(v[0],dic,courseDict)

                del dic[v[0]]
                if res == False:
                    return res
        return True

sol = Solution()
res = sol.canFinish(4,[[0,1],[3,1],[1,3],[3,2]])
print res
res = sol.canFinish(3,[[1,0],[0,1]])
print res
