import io
import sys

_INPUT = """\
6
3 998244353
16 999999937
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import copy
  N,P=map(int,input().split())
  dp=[[0]*2 for j in range(N)]
  dp[0][0]=1
  dp[1][1]=1
  for i in range(N-1):
    tmp=[[0]*2 for j in range(N)]
    for j in range(N):
      tmp[j][0]=(tmp[j][0]+dp[j][0]+dp[j][1])%P
      if j<N-1:
        tmp[j+1][0]=(tmp[j+1][0]+3*dp[j][0])%P
        tmp[j+1][1]=(tmp[j+1][1]+dp[j][1])%P
      if j<N-2: tmp[j+2][1]=(tmp[j+2][1]+2*dp[j][0])%P
    dp=tmp
  print(*[dp[i+1][0] for i in range(N-1)])