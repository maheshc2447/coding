n=list(map(int,input().split())) #reading the input
a=n[0] #assigning index 0 to a variable
s=[]  
s=n[a:]+n[:a] #using slicing method we rotated the array
for i in s:
    print(i,end="")
  
