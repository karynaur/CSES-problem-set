n=int(input())
if n==1:
  print(0)
  exit()
arr=list(map(int,input().split()))
count=0

for i in range(1,n):
  c=arr[i]-arr[i-1]
  
  if c<0:
    count+=abs(c)
    arr[i]=arr[i-1]
  
print(count)

