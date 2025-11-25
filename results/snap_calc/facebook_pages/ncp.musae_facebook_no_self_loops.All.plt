#
# Graph: ../../graph-ncp-project/datasets/facebook_pages/musae_facebook_no_self_loops.txt -> musae_facebook_no_self_loops musae_facebook_no_self_loops A=0.001, K=1000-1.5-100M, Cvr=10, SzFrc=0.001 G(19153, 167137) (Tue Nov 25 13:20:29 2025)
#

set title "Graph: ../../graph-ncp-project/datasets/facebook_pages/musae_facebook_no_self_loops.txt -> musae_facebook_no_self_loops musae_facebook_no_self_loops A=0.001, K=1000-1.5-100M, Cvr=10, SzFrc=0.001 G(19153, 167137)"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "k (number of nodes in the cluster)"
set ylabel "Normalized community score (lower is better)"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'ncp.musae_facebook_no_self_loops.All.png'
plot 	"ncp.musae_facebook_no_self_loops.INFO.tab" using 1:4 title "Conductance" with lines lw 2,\
	"ncp.musae_facebook_no_self_loops.INFO.tab" using 1:5 title "Expansion" with points pt 3,\
	"ncp.musae_facebook_no_self_loops.INFO.tab" using 1:6 title "Internal Density" with points pt 5 ps 0.8,\
	"ncp.musae_facebook_no_self_loops.INFO.tab" using 1:7 title "Cut Ratio" with points pt 6,\
	"ncp.musae_facebook_no_self_loops.INFO.tab" using 1:8 title "Normalized Cut" with points pt 7,\
	"ncp.musae_facebook_no_self_loops.INFO.tab" using 1:9 title "Maximum FDO" with points pt 9,\
	"ncp.musae_facebook_no_self_loops.INFO.tab" using 1:10 title "Avg FDO" with points pt 11,\
	"ncp.musae_facebook_no_self_loops.INFO.tab" using 1:13 title "Flake FDO" with points pt 13
