from collections import deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        litter = {}
        start_r = start_c = 0
        idx = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = idx
                    idx += 1

        k = idx
        target = (1 << k) - 1

        # best[(r,c,mask)] = maximum energy seen
        best = {}

        q = deque()
        q.append((start_r, start_c, energy, 0, 0))

        best[(start_r, start_c, 0)] = energy

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, e, mask, dist = q.popleft()

            if mask == target:
                return dist

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                if e == 0:
                    continue

                ne = e - 1

                if classroom[nr][nc] == 'R':
                    ne = energy

                nmask = mask

                if (nr, nc) in litter:
                    nmask |= (1 << litter[(nr, nc)])

                state = (nr, nc, nmask)

                if best.get(state, -1) >= ne:
                    continue

                best[state] = ne
                q.append((nr, nc, ne, nmask, dist + 1))

        return -1