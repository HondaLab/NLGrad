# NLGrad
Online learning in Gradient method for Non-Linear model function.
$\lambda$ is forgetting factor and the vale is set 0.5 as typical case.


$Q' = \lambda Q + (f(x_i)-y_i)^2$

## MInfo_1a.py
相互情報量: I(X;Y) = sum_{xy} p(x,y) log p(x,y)/(p(x)p(y))

## dist2b.py
p(x,y)を求める

<img src='https://github.com/HondaLab/NLGrad/blob/honda/pics/dist2b.png' width=600>

## dist2a.py
x,yデータから分布関数p(x),p(y)を求める．


## nlgrad4b.py
生成したデータをファイルに出力する

## nlgrad4a.py
勾配法
Q'_alpha = lambda*Q_alpha -2(y_i-f(x_i))*df/d alpha
Q'_beta = lambda*Q_beta -2(y_i-f(x_i))*df/d beta
Q'_b = lambda*Q_b -2(y_i-f(x_i))*df/d b


alpha'=alpha-|alpha|*eta*Q_alpha
beta'=beta-|beta|*eta*Q_beta
b'=b-|b|*eta*Q_b

<img src='https://github.com/HondaLab/NLGrad/blob/honda/pics/sample4a.png' width=600>

gradd3a.py
最急降下法でtanh関数のパラメータをオンライン学習する
x:説明変数を一様にランダムに生成する．
lambda(忘却係数)=0.5


