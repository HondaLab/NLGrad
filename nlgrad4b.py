#!/usr/bin/python3
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib

DATA_FILE="data_normal_1a.xy"
PRM_FILE="tanh_1a.prm"


def plot(x_min,x_max,func,sx,sy,alpha,beta,b):
   n_last=10
   n_plt=1000
   plt_sx=sx[len(sx)-n_plt:len(sx)]
   plt_sy=sy[len(sy)-n_plt:len(sy)]
   last_sx=sx[len(sx)-n_last:len(sx)]
   last_sy=sy[len(sy)-n_last:len(sy)]
   px=[]
   py=[]
   py2=[]
   dx=0.1
   x=x_min
   while x<=x_max:
      px.append(x)
      py.append(func(x,alpha,beta,b))
      #py2.append(func_beta(x,alpha,beta,b))
      x+=dx
   #plt.xlim(x_min,x_max)
   plt.scatter(plt_sx,plt_sy,c="orange")
   plt.scatter(last_sx,last_sy,c="red")
   plt.plot(px,py)
   #plt.plot(px,py2,c="red")
   plt.show()

def func(x,alpha,beta,b):
   f=alpha*np.tanh(beta*(x-b))
   return f

def func_alpha(x,alpha,beta,b):
   f=np.tanh(beta*(x-b))
   return f

def func_beta(x,alpha,beta,b):
   f=alpha*(x-b)/np.cosh(beta*(x-b))**2
   return f

def func_b(x,alpha,beta,b):
   f=-alpha*beta/np.cosh(beta*(x-b))**2
   return f

alpha_o=60.0
beta_o=0.15
b_o=270.0
error=25.0
eta=0.00001 # 学習係数
lmbda=0.7 # 忘却係数
N=5000    # データ数

fp=open(DATA_FILE,"a")
fp_prm=open(PRM_FILE,"r")
for line in fp_prm:
   #print(line)
   item = line.split(",")
   if item[0][0]!="#":
      alpha=float(item[0])
      beta=float(item[1])
      b=float(item[2])
      Q_min=float(item[3])
      print("alpha=%8.5f " % alpha,end='')
      print("beta=%8.5f " % beta,end='')
      print("b=%8.5f " % b,end='')
      print("Q_min=%8.5f " % Q_min,end='')
      print(item[4],end='')
fp_prm.close()

px=[]
py1=[]
py2=[]

dx=1
x_min=b_o-100.0
x_max=b_o+100.0
Q=1.0
Qalpha=0.0
Qbeta=0.0
Qb=0.0

alpha_best=alpha
beta_best=beta
b_best=b

fp.write("#        x          y \n")
i=1
while i<=N:
   x=x_min+random.random()*(x_max-x_min)
   #x=np.random.normal(b_o,40,1)
   e=np.random.normal(0,0.3*alpha_o,1) # 誤差を正規分布で生成
   #e=2.0*(random.random()-0.5)*error
   y=func(x,alpha_o,beta_o,b_o)
   y2=y+e # as data
   fp.write("%10.4f, %10.4f \n" % (x,y2))

   px.append(x)
   py1.append(y)
   py2.append(y2)

   if i%10==0:
      plot(x_min,x_max,func,px,py2,alpha,beta,b)

   dum=-2.0*(y2-func(x,alpha,beta,b))
   #print("i/N=%3d/%3d, " %(i,N),end='')
   #print("x=%8.5f, dum=%8.5f" % (x,dum) )
   #q=input("Input any to continue.")
   try:
      Qalpha=lmbda*Qalpha+dum*func_alpha(x,alpha,beta,b) 
      Qbeta =lmbda*Qbeta +dum*func_beta(x,alpha,beta,b) 
      Qb    =lmbda*Qb    +dum*func_b(x,alpha,beta,b) 
   except:
      pass

   alpha=alpha -np.abs(alpha)*eta*Qalpha
   beta=beta -np.abs(beta)*eta*Qbeta
   b=b -np.abs(b)*eta*Qb

   Q=lmbda*Q+np.power((y2-func(x,alpha,beta,b)),2)
   #print("Q_new=%6.3e " % (Q_new),end='')
   
   '''
   # これをやったら良くなると感じるけど，実際はダメ
   if i>100 and Q>Q_min:
      Q=Q_min
      alpha=alpha_best
      beta=beta_best
      b=b_best
   '''

   if Q<Q_min and i>1 :
      Q_min=Q
      alpha_best=alpha
      beta_best=beta
      b_best=b

   print("\r i/N:%5d/%5d, Q=%6.3e " % (i,N,Q),end='')
   print("alpha=%6.3f " % (alpha),end='')
   print("beta=%6.3f " % (beta),end='')
   print("b=%6.3f " % (b),end='')

   i+=1

print("\n Q_min=%6.3e " % (Q_min),end='')
print("alpha_best=%6.3f " % (alpha_best),end='')
print("beta_best=%6.3f " % (beta_best),end='')
print("b_best=%6.3f " % (b_best),end='')

fp_prm=open(PRM_FILE,"a")
fp_prm.write("#   alpha,    beta,       b,        Q \n")
fp_prm.write(" %8.3f, %8.3f, %8.3f, %8.3f, " % (alpha_best,beta_best,b_best,Q_min))
fp_prm.write(" best \n")
fp_prm.write(" %8.3f, %8.3f, %8.3f, %8.3f, " % (alpha,beta,b,Q))
fp_prm.write(" current \n")
fp.close()
fp_prm.close()

Q=0.0
i=1
while i<=N:
   Q+=(py1[i-1]-py2[i-1])**2
   i+=1
print(np.sqrt(Q/N))


'''
plt.scatter(px,py1)
plt.scatter(px,py2)
plt.show()
'''
