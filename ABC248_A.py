import io
import sys

_INPUT = """\
6
023456789
459230781
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  for i in range(10):
    if str(i) not in S: print(i)