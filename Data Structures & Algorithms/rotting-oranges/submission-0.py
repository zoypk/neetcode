#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Medium (55.95%)
# Likes:    14632
# Dislikes: 462
# Total Accepted:    1.4M
# Total Submissions: 2.5M
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# You are given an m x n grid where each cell can have one of three
# values:
#
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
#
#
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten
# orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange. If this is impossible, return -1.
#
#
# Example 1:
#
#
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#
#
# Example 2:
#
#
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
#
#
# Example 3:
#
#
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer
# is just 0.
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
#
#
#

from ll import deque


# @lc code=start
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # So we will first fill the q with rotten cords
        # then we will iterate the q len(q) times ( classic bfs )
        # then we will go through all dirs ( classic graph )
        # and mark them as rotten and time+=1
        # now when we mark them as rotten we need to add them to q and after each iteration remove the current rotten ones

        q = deque()
        time = 0
        oranges = 0

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    oranges += 1  # This is to identify if there is an isolated fresh 🍊
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q and oranges > 0:
            level_size = len(q)
            for _ in range(level_size):
                r, c = q.popleft()

                for dr, dc in DIRECTIONS:
                    rd, cd = r + dr, c + dc
                    if 0 <= rd < ROWS and 0 <= cd < COLS and grid[rd][cd] == 1:
                        grid[rd][cd] = 2
                        q.append((rd, cd))
                        oranges -= 1
            time += 1

        return time if not oranges else -1


# @lc code=end
