from maplotlib import pyplot as plt
def midpoint (x0,y0,x1,y1)
 dx=abs (x1-x0)
 dY=abs(y1-y0)
 x=x0
 y=y0
 xlist=[x]
 ylist=[y]
 print(("x=",x,end,end=" ")
 print("x=",x,end="\n")
 d=dy-(dx/2)
 while(x<x1):

 x=x+1
 if(d<0):
  d==d+dy
  else:
  d=d+dy - dx
  y=y+1
  xlist.append(x)
  ylist.append(y)
  plt.plot(xlist,ylist,linestyle="--",marker="+")
  plt show()
#main
print("Enter Initial Point")
x0=int(input())
y0=int(input())
print("Enter Finishing Point")
x1=int(input())
y1=int(input())
DDA(x0,y0,x1,y1)