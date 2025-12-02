#
# Graph: ../../../datasets/facebook_pages/musae_facebook_no_self_loops.txt -> musae_facebook_no_self_loops musae_facebook_no_self_loops. A=0.001, K=1000-1.5-100M, Cvr=10, SzFrc=0.001 G(19153, 167137) (Tue Nov 25 16:30:16 2025)
#

set title "Graph: ../../../datasets/facebook_pages/musae_facebook_no_self_loops.txt -> musae_facebook_no_self_loops musae_facebook_no_self_loops. A=0.001, K=1000-1.5-100M, Cvr=10, SzFrc=0.001 G(19153, 167137)"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "k (number of nodes in the cluster)"
set ylabel "{/Symbol \F} (conductance)"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'ncp.musae_facebook_no_self_loops.png'
plot 	"ncp.musae_facebook_no_self_loops.tab" using 1:2 title "ORIGINAL MIN (19153, 167137)" with lines lw 1
