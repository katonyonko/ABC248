import io
import sys

_INPUT = """\
6
2 3 4
31 41 592
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  N,M,K=map(int,input().split())
  dp=[0]*(K+1)
  dp[0]=1
  for i in range(N):
    tmp=[0]*(K+1)
    for j in range(M):
      for k in range(K+1):
        if j+1+k<K+1: tmp[j+1+k]=(tmp[j+1+k]+dp[k])%mod
    dp=tmp
  print(sum(dp)%mod)