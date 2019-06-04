#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<getopt.h>
#include<math.h>
double mylogistic( double x);
double myorbit(double t, double EPS, double y0, double yprime0);

int main(){
for (double x=0; x<=3;x+=0.05) {fprintf(stdout,"%.8g\t%.8g\t%.8g\n",x,mylogistic(x),1/(1+exp(-x)));}

double eps[3] = {0,0,0.1};
double y0[3]  = {1,1,1};
double yprime[3] = {0,0.5,0.5};

for(double phi=0;phi<=4*2*M_PI;phi+=0.05)
	fprintf(stderr,"%g\t%g\t%g\t%g\n",phi,myorbit(phi,eps[0],y0[0],yprime[0]),
                                          myorbit(phi,eps[1],y0[1],yprime[1]),
                                          myorbit(phi,eps[2],y0[2],yprime[2]));


return EXIT_SUCCESS;
}