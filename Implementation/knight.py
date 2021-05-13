n = input()
row = int(n[1])
col = int(ord(n[0])-ord('a'))+1

steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

cnt = 0
for step in steps:
  nrow = row + step[0]
  ncol = col + step[1]

  if nrow>=1 and nrow<=8 and ncol>=1 and ncol<=8:
    cnt += 1
print(cnt)


