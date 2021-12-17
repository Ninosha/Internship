
# 3
def printGrid(grid) :
    for row in grid :
        print("".join(row))

r, c, n = [int(i) for i in input().strip().split()]
D = [['O' for i in range(c)] for j in range(r)]

G = []
for _ in range(r) :
    G.append(list(input()))

S3 = [['.' for i in range(c)] for j in range(r)]
for i in range(r) :
    for j in range(c) :
        if not ((j+1<c and G[i][j+1]=='O') or (j-1>=0 and G[i][j-1]=='O') or (i-1>=0 and G[i-1][j]=='O') or (i+1<r and G[i+1][j]=='O')) :
            if(G[i][j]!='O') : S3[i][j] = 'O'

S5 = [['.' for i in range(c)] for j in range(r)]
for i in range(r) :
    for j in range(c) :
        if not ((j+1<c and S3[i][j+1]=='O') or (j-1>=0 and S3[i][j-1]=='O') or (i-1>=0 and S3[i-1][j]=='O') or (i+1<r and S3[i+1][j]=='O')) :
            if (S3[i][j]!='O'): S5[i][j] = 'O'

if n%2==0 :
    printGrid(D)
elif n==1  :
    printGrid(G)
elif (n+1)%4==0 :
    printGrid(S3)
else :
    printGrid(S5)