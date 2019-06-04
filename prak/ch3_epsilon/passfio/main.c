#include<stdio.h>
#include<math.h>

int make_table(double (*f)(double), int n, double* x){
	for(int i=0;i<n;i++){
		printf("%g %g\n", x[i],f(x[i]));
	}
return 0;
}

double (*fun)(double);
double z;

int main(){
	fun=sin;
	const int n=5;
	double x[n];
	for(int i=0;i<n;i++)x[i]=i;
	make_table(fun,n,x);
	make_table(sin,n,x);
	make_table(cos,n,x);
	make_table(tgamma,n,x);
	
return 0;
}