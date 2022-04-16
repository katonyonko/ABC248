import io
import sys

_INPUT = """\
6
5
3 1 4 1 5
4
1 5 1
2 4 3
1 5 2
1 3 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  Q=int(input())
  a=[0]*N
  query=[[] for _ in range(N+1)]
  ans=[0]*Q
  for i in range(Q):
    L,R,X=map(int,input().split())
    L-=1;X-=1
    query[L].append((X,-1,i))
    query[R].append((X,1,i))
  for i in range(N+1):
    for X,sign,idx in query[i]:
      ans[idx]+=a[X]*sign
    if i<N:
      a[A[i]-1]+=1
  for i in range(Q):
    print(ans[i])