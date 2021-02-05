f=open("test_input (1).txt","r")
lines=f.readlines()
numbers =[list(map(int,e.strip().split())) for e in lines]



t=open("test_output.txt","r")
goal=[repr(e)  for e in t.readlines()]




print(goal)
