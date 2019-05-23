from matrix import matrix,vector
v=vector([1,2,3])
for i in v: print(i)
v.print("v=")
n=3
m=matrix(2,2)
m[0,0]=0
m[0,1]=1
m[1,0]=2
m[1,1]=3

m.print("m=")
m[:,0].print(":,0 = ")
m[:,1].print(":,1 = ")