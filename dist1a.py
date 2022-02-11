import numpy as np

READ_FILE="data_normal_1a.xy"

fp=open(READ_FILE,'r')
cnt=0
for line in fp:
   if line[0]!="#":
      item=line.split(",")
      x=float(item[0])
      y=float(item[1].strip("\n"))
      cnt+=1
      #print(cnt,x,y)
      if cnt==1:
         x_min=x
         x_max=x         
         y_min=y
         y_max=y         
      if x<x_min: x_min=x
      if x>x_max: x_max=x
      if y<y_min: y_min=y
      if y>y_max: y_max=y
fp.close()

N=cnt
print("# Num of data=%8d" % N)
print("# x_min=%8.3f, x_max=%8.3f" % (x_min,x_max))
print("# y_min=%8.3f, y_max=%8.3f" % (y_min,y_max))

bin_N=int(np.log2(cnt))+1 # スタージェスの公式でビンの数を決める．
print("# bin_N=%4d" % bin_N)

dx=(x_max-x_min)/bin_N
x_bin=[]
x=x_min
for i in range(bin_N):
   x_bin.append(x)
   x+=dx
x_bin.append(x_max)
#print(x_bin)

dy=(y_max-y_min)/bin_N
y_bin=[]
y=y_min
for i in range(bin_N):
   y_bin.append(y)
   y+=dy
y_bin.append(y_max)
#print(y_bin)

fp=open(READ_FILE,'r')
pop_x=[0]*(bin_N+1)
pop_y=[0]*(bin_N+1)
cnt=0
for line in fp:
   if line[0]!="#":
      item=line.split(",")
      x=float(item[0])
      y=float(item[1].strip("\n"))
      #print(x,y)
      cnt+=1
      i=0
      while x>x_bin[i]:
         i+=1
      pop_x[i-1]=pop_x[i-1]+1
      i=0
      while y>y_bin[i]:
         i+=1
      pop_y[i-1]=pop_y[i-1]+1
      #print(y,y_bin[i])
fp.close()

print("# Population ")
x_cnt=0
y_cnt=0
for i in range(bin_N):
   print("%8.3f %8.3f %8.3f %8.3f " % (x_bin[i],pop_x[i],y_bin[i],pop_y[i]))
   x_cnt+=pop_x[i]
   y_cnt+=pop_y[i]
#print(x_cnt,y_cnt,N)
