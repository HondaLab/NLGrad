#!/usr/bin/python3
# dist2a.py: Let each process put in function
import numpy as np

def Maxmin(file_name):
   fp=open(file_name,'r')
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

   return N,x_min,x_max,y_min,y_max

def Make_bin(N,x_min,x_max,y_min,y_max):
   N_bin=int(np.log2(N))+1 # スタージェスの公式でビンの数を決める．
   print("# N_bin=%4d" % N_bin)

   dx=(x_max-x_min)/N_bin
   x_bin=[]
   x_label=[]
   x=x_min
   for i in range(N_bin):
      x_bin.append(x)
      x_label.append(str("%5d" % x))
      x+=dx
   x_bin.append(x_max)
   x_label.append(str("%5d" % x_max))
   #print(x_bin)

   dy=(y_max-y_min)/N_bin
   y_bin=[]
   y_label=[]
   y=y_min
   for i in range(N_bin):
      y_bin.append(y)
      y_label.append(str("%5.2f" % y))
      y+=dy
   y_bin.append(y_max)
   y_label.append(str("%5.2f" % y_max))
   #print(y_bin)

   return N_bin,x_bin,y_bin,x_label,y_label

def Distribution(file_name,N_bin,x_bin,y_bin):
   fp=open(file_name,'r')
   pop_x=[0]*(N_bin+1)
   pop_y=[0]*(N_bin+1)
   pop_xy=[[0]*(N_bin+1) for i in range(N_bin+1)]
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
         j=0
         while y>y_bin[j]:
            j+=1
         pop_y[j-1]=pop_y[j-1]+1
         pop_xy[i-1][j-1]=pop_xy[i-1][j-1]+1
   
         #print(y,y_bin[i])
   fp.close()

   print("# Population ")
   x_cnt=0
   y_cnt=0
   xy_cnt=0
   for i in range(N_bin):
      #print("%8.3f %8.3f %8.3f %8.3f " % (x_bin[i],pop_x[i],y_bin[i],pop_y[i]))
      x_cnt+=pop_x[i]
      y_cnt+=pop_y[i]
      for j in range(N_bin):
         xy_cnt+=pop_xy[i][j]

   N_x=x_cnt
   N_y=y_cnt
   N_xy=xy_cnt
   #print(N_x,N_y,N_xy,N)

   #print("# Distribution ")
   dist_x=[0]*(N_bin+1)
   dist_y=[0]*(N_bin+1)
   dist_xy=[[0]*(N_bin+1) for i in range(N_bin+1)]
   integ_x=0.0
   integ_y=0.0
   integ_xy=0.0
   for i in range(N_bin):
      dist_x[i]=pop_x[i]/N_x
      dist_y[i]=pop_y[i]/N_y
      integ_x+=dist_x[i]
      integ_y+=dist_y[i]
      #print("%8.3f %8.3f " % (x_bin[i],dist_x[i]),end='')
      #print("%8.3f %8.3f " % (y_bin[i],dist_y[i]))
      for j in range(N_bin):
         dist_xy[i][j]=pop_xy[i][j]/N_xy
         integ_xy+=dist_xy[i][j]

   #print("%12.7f %12.7f %12.7f" % (integ_x,integ_y,integ_xy))
   return dist_x,dist_y,dist_xy

if __name__=="__main__":
   import matplotlib.pyplot as plt
   import pandas as pd
   import seaborn as sns

   DATA_FILE="data_normal_1a.xy"
   print("# In '%s'" % DATA_FILE)
   N,x_min,x_max,y_min,y_max=Maxmin(DATA_FILE)
   N_bin,x_bin,y_bin,x_label,y_label=Make_bin(N,x_min,x_max,y_min,y_max)
   dist_x,dist_y,dist_xy=Distribution(DATA_FILE,N_bin,x_bin,y_bin)
   show=[[0]*(N_bin+1) for i in range(N_bin+1)]

   print("# Distribution ")
   print("#      x     p(x)        y     p(y)")
   integ_x=0.0
   integ_y=0.0
   integ_xy=0.0
   for i in range(N_bin+1):
      integ_x+=dist_x[i]
      integ_y+=dist_y[i]
      #print("%8.3f %8.5f " % (x_bin[i],dist_x[i]),end='')
      #print("%8.3f %8.5f " % (y_bin[i],dist_y[i]))
      for j in range(N_bin+1):
         integ_xy+=dist_xy[i][j]
         show[j][i]=dist_xy[i][j]
         #print("%8.3f %8.3f %8.5f " % (x_bin[i],y_bin[j],dist_xy[i][j]))
      #print("\n")

   print("# Intg_x p(x)=%8.5f Intg_y p(y)=%8.5f Intg_xy p(x,y)=%8.5f" % (integ_x,integ_y,integ_xy))
 
   df=pd.DataFrame(data=show, index=y_label, columns=x_label)
   ax=sns.heatmap(df)
   ax.invert_yaxis()
   plt.show()
