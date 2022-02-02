import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib

#matplotlib.use('wxagg')

def plot(x_min,x_max,func,sx,sy,alpha,beta,b):
   n_last=10
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
   plt.scatter(sx,sy,c="orange")
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
beta_o=0.08
b_o=270.0
error=15.0
eta=0.001 # 学習係数
lmbda=0.5 # 忘却係数
N=5000    # データ数


px=[]
py1=[]
py2=[]

dx=1
x_min=b_o-250.0
x_max=b_o+250.0
Q=1.0
Q_min=1.0e10
Qalpha=0.0
Qbeta=0.0
Qb=0.0
alpha=50
beta=1.00
b=b_o+50

alpha_best=alpha
beta_best=beta
b_best=b
print("alpha=%8.5f " % alpha,end='')
print("beta=%8.5f " % beta,end='')
print("b=%8.5f " % b)
i=1
while i<=N:
   x=x_min+random.random()*(x_max-x_min)
   #x=np.random.normal(b_o,40,1)
   e=2.0*(random.random()-0.5)*error
   y=func(x,alpha_o,beta_o,b_o)
   y2=y+e # as data

   px.append(x)
   py1.append(y)
   py2.append(y2)

   if i%10==0:
      plot(x_min,x_max,func,px,py2,alpha,beta,b)

   dum=-2.0*(y2-func(x,alpha,beta,b))
   print("i/N=%3d/%3d, " %(i,N),end='')
   print("x=%8.5f, dum=%8.5f" % (x,dum) )
   #q=input("Input any to continue.")
   Qalpha=lmbda*Qalpha+dum*func_alpha(x,alpha,beta,b) 
   Qbeta =lmbda*Qbeta +dum*func_beta(x,alpha,beta,b) 
   Qb    =lmbda*Qb    +dum*func_b(x,alpha,beta,b) 

   alpha=alpha -5.0*eta*Qalpha
   beta=beta -0.01*beta*eta*Qbeta
   b=b -1.0*eta*Qb

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

   if Q<Q_min and i>1000 :
      Q_min=Q
      alpha_best=alpha
      beta_best=beta
      b_best=b

   print("Q(Q_min)=%6.3e(%4.1e) " % (Q,Q_min),end='')
   print("alpha=%6.3f(%4.1f) " % (alpha,alpha_best),end='')
   print("beta=%6.3f(%4.2f) " % (beta,beta_best),end='')
   print("b=%6.3f(%5.1f) " % (b,b_best))

   i+=1
print(np.sqrt(Q))

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
