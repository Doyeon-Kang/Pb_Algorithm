"""
1) 아이디어
BFS: 너비우선탐색 

2) 시간복잡도
BFS: O(V+E)

3) 자료구조
Queue(양방향 큐)
"""

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)] # map = [[1 1 0 1 1],[0 1 1 0 0]...] 
cnt = 0
maxv = 0

chk = [list(False for _ in range(n))]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1] #아래 오른쪽 위 왼쪽 

def bfs(y, x):
  rs = 1
  q = deque()
  q.append((y, x))
  while q:
    ey, ex = q.popleft()
    for k in range(4):
      ny = map[ey + dy[k]]
      nx = map[ex + dx[k]]
      if 0 <= ny < n and 0 <= nx < m:
        if map[ny][nx] == 1 and chk[ny][nx] == False: 
          q.append(ny, nx)
          rs += 1
    return rs


for i in range(n):
  for j in range(m):
    if map[i][j] == 1 and chk[i][j] == False:
      chk[i][j] = True
      cnt += 1
      maxv = max(maxv, bfs(i, j))

print(cnt)
print(maxv)