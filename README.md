# NLGrad
Online learning in Gradient method for Non-Linear model function.
$\lambda$ is forgetting factor and the vale is set 0.5 as typical case.


$Q' = \lambda Q + (f(x_i)-y_i)^2$

## dist2b.py
p(x,y)を求める

## dist2a.py
x,yデータから分布関数p(x),p(y)を求める．

## nlgrad4b.py
生成したデータをファイルに出力する

## nlgrad4a.py

alpha=(1-eta*Qalpha)
beta=(1-eta*Qbeta)
b=(1-eta*Qb)

<img src='https://github.com/HondaLab/NLGrad/blob/honda/pics/sample4a.png' width=600>

gradd3a.py
最急降下法でtanh関数のパラメータをオンライン学習する
x:説明変数を一様にランダムに生成する．
lambda(忘却係数)=0.5


