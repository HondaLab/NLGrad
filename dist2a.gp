set term post eps color 
set output 'dist2a.eps'
set title 'y=alpha tanh beta(x-b)'
set label 'alpha=60' at -130,0.18
set label 'beta=0.15' at -130,0.17
set label 'b=270' at -130,0.16
set xlabel 'y'
set ylabel 'p(y)'
set yrange [0:0.2]
plot 'dist.xy' u 3:4 w boxes
