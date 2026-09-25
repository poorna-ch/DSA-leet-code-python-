from collections import deque

class Solution(object):
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1":
                    count += 1

                    q = deque()
                    q.append((r, c))
                    grid[r][c] = "0"

                    while q:
                        row, col = q.popleft()

                        directions = [
                            (-1, 0),   # up
                            (1, 0),    # down
                            (0, -1),   # left
                            (0, 1)     # right
                        ]

                        for dr, dc in directions:
                            nr = row + dr
                            nc = col + dc

                            if (0 <= nr < rows and
                                0 <= nc < cols and
                                grid[nr][nc] == "1"):

                                q.append((nr, nc))
                                grid[nr][nc] = "0"

        return count