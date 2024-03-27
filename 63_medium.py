#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 13:42:04 2024

@author: tonyyao
"""
# https://leetcode.com/problems/unique-paths-ii/

#slow
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [ [0 for _ in range(n)] for _ in range(m)] 
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0
        if m == 1 and n == 1:
            return 1
        
        if m == 1:
            return self.uniquePathsWithObstacles([obstacleGrid[0][1:]])
        
        if n == 1:
            return self.uniquePathsWithObstacles(obstacleGrid[1:])

        return self.uniquePathsWithObstacles([obstacleGrid[x][1:] for x in range(m)]) + self.uniquePathsWithObstacles(obstacleGrid[1:])

#Leetcode NOT accepted, but works fine at local.
class Solution:
    dp = dict()
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if m == 1 and n == 1:
            if obstacleGrid[0][0] == 0:
                self.dp[(m, n)] = 1
            else:
                self.dp[(m, n)] = 0
        elif obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            self.dp[(m, n)] = 0
        elif m == 1:
            if (m, n - 1) not in self.dp.keys():
                self.dp[(m, n - 1)] = self.uniquePathsWithObstacles([obstacleGrid[0][1:]])
            self.dp[(m, n)] = self.dp[(m, n - 1)]
        elif n == 1:
            if (m - 1, n) not in self.dp.keys():
                self.dp[(m - 1, n)] = self.uniquePathsWithObstacles(obstacleGrid[1:])
            self.dp[(m, n)] = self.dp[(m - 1, n)]
        else:
            if (m, n - 1) not in self.dp.keys():
                self.dp[(m, n - 1)] = self.uniquePathsWithObstacles([obstacleGrid[x][1:] for x in range(m)])
            if (m - 1, n) not in self.dp.keys():
                self.dp[(m - 1, n)] = self.uniquePathsWithObstacles(obstacleGrid[1:])
            self.dp[(m, n)] = self.dp[(m, n - 1)] + self.dp[(m - 1, n)]
        return self.dp[(m, n)]

#fast
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        if m == 1 and n == 1:
            return 1
        
        dp = [ [0 for _ in range(n)] for _ in range(m)] 
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i - 1][0]
                elif i == 0 and j > 0:
                    dp[i][j] = dp[0][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
        return dp[m - 1][n - 1]
                    
if __name__ == '__main__':
    obstacleGrid = [[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],[1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],[0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],[1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],[0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],[1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))
