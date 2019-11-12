%enter list sizes 
n = [256, 1024, 4096, 16384, 65536,262144];
%put experimental values for timing 
exp_time_insertion_sort = [0.00000204, 0.00002849, 0.000515, 0.0107, 0.13, 2.014];
%enter experimental C value
C_insertion_sort=0.0000000000297;  
%calculate theoretical insertion sort values
theory_insertionsort = C_insertion_sort* n.^2.;
figure(1)
clf
%plot the data
plot( n, exp_time_insertion_sort, 'ro' )

hold on

plot( n, theory_insertionsort, 'b-' )

hold off

legend( ' experimental sort  ', 'theory sort ', 'Location', 'northwest')
%set x and y axis labels and title
xlabel( ' list length n ' )
ylabel( ' f(n) in sec' )
title( 'Insertion Sort in regular axes  ' )

set( gcf, 'Color', [ 1 1 1 ] )
%figure 2 for log axes
figure(2)
clf
loglog( n, exp_time_insertion_sort, 'ko' )      
hold on   
loglog( n, theory_insertionsort, 'r-' )
hold off
%set axis label
xlabel('log(n)')
ylabel('log(f(n))')
%set axis title
title('Insertion Sort  log-log Axes')
%set axis legend

legend( 'experimental insertion sort','theory insertion sort','Location', 'northwest')

axis tight

