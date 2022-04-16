import io
import sys

_INPUT = """\
6
1 4 2
7 7 10
31 415926 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B,K=map(int,input().split())
  ans=0
  while A<B:
    ans+=1
    A*=K
  print(ans)