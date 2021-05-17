n,m = map(int, input().split())

# 맵 방문 위치 저장 위한 맵 생성 
d = [[0]* m for _ in range(n)]

x,y,dir = map(int, input().split())
d[x][y] = 1 # 시작점 현재위치 방문처리

# map 바다/육지 입력받기
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
  global dir
  dir -= 1
  if dir == -1:
    dir = 3

cnt = 1
turn_cnt = 0

while True:
  turn_left()
  nx = x+dx[dir]
  ny = y+dy[dir]

  # 회전 이후 정면에 가보지 않은 칸 존재하는 경우 이동
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny]=1
    x = nx
    y = ny
    cnt += 1
    turn_cnt = 0
    continue
# 회전 이후 정면에 가보지 않은 칸이 없거나 바다인 경우 
  else:
    turn_cnt += 1
# 네 방향 모두 갈 수 없는 경우
  if turn_cnt == 4:
    nx = x-dx[dir]
    ny = y-dy[dir]
    # 후진 가능
    if array[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn_cnt = 0

print(cnt)








