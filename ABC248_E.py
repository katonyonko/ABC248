import io
import sys

_INPUT = """\
6
5 2
0 0
1 0
0 1
-1 0
0 -1
1 1
0 0
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import math
  N,K=map(int,input().split())
  points=[list(map(int,input().split())) for _ in range(N)]
  if K==1: print('Infinity')
  else:
    ans=0
    lines=set()
    for i in range(N):
      a,b=points[i]
      for j in range(i+1,N):
        c,d=points[j]
        if a==c: lines.add((a,-1,-1,-1))
        else:
          p,q,r,s=d-b,c-a,b*c-a*d,c-a
          p,q,r,s=p//math.gcd(p,q),q//math.gcd(p,q),r//math.gcd(r,s),s//math.gcd(r,s)
          if q<0: p*=-1; q*=-1
          if s<0: r*=-1; s*=-1
          lines.add((p,q,r,s))
    for p,q,r,s in lines:
      tmp=0
      for x,y in points:
        if q==-1 and x==p: tmp+=1
        if q!=-1 and p*s*x+q*r-q*s*y==0: tmp+=1
      if tmp>=K: ans+=1
    print(ans)