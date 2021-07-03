# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

class Solution:
    def allPathsSourceTarget(self, graph: list) -> list:
        q = [[0]]
        result = []
        target = len(graph) - 1
        
        while q:
            temp = q.pop()
            if temp[-1] == target:
                result.append(temp)
            else:
                for neighbor in graph[temp[-1]]:
                    q.append(temp + [neighbor])
        
        return result