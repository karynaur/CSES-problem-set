#n=int(input())
import numpy

def sigmoid(x):
  return 1 / (1 + numpy.exp(-x))

#for i in range(n):
a=list(map(int,input().strip().split()))
x=a[0]*-28705012.10456237+a[1]*-29963431.02309792


if numpy.round(sigmoid(x))==1:
  print("YES")
else: print("NO")
