n=int(input())
if n==1:
  print(1)
  exit()
if n==2 or n==3 or n==0: 
  print("NO SOLUTION")
  exit()
i=2
for j in range(n):
    
    print(i,end=" ")
    if i+2<=n:i+=2
    else:
      if n%2==0: 
        i=abs(n-i)+1
      else:
        i=abs(n-i)



