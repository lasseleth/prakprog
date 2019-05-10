#include<limits.h>
#include<float.h>
#include<math.h>
#include<stdio.h>

int main(){

//Opgave 1i

	int a=INT_MAX;
	printf("\n Exercise I a\n Int_Max = %i\n",a);

	int b=1; while(b+1>b) {b++;}
	printf("max int while = %i\n",b);

	int c;
	for(c=1;c+1>c;c++){c;};
        printf("max int for = %i\n",c);
		
	int d=1;
	do {d++;}
	while(d+1>d);
	printf("max int do while = %i\n \n",d);

//Opgave 1ii
	int e=INT_MIN;
	printf("\n Exercise I b\n Int_Min=%i\n",e);

	int f1=1; while(f1-1<f1) {f1++;}
	printf("min int while = %i\n",f1);

	int g;
	for(g=1; g-1<g;g++){g;}
	printf("min int for = %i\n",g);

	int h=1;
	do{h++;}
	while(h-1<h);
	printf("min int do while= %i\n \n",h);

//Opgave 1iii

	double i=DBL_EPSILON;
	printf("\n Exercise I c\n DBL_EPSILON=%g\n",i);

	double j=1;
	while(1+j!=1){j/=2;} j*=2;
	printf("double epsilon while=%g\n",j);
    
	double k=1;
	do {k/=2;}
	while(1+k!=1);
	k*=2;
	printf("double epsilon do while=%g\n",k);

	double l=1;
	for(l=1; 1+l!=1; l/=2){} l*=2;
	printf("double epsilon for=%g\n",l);

	float m=FLT_EPSILON;
	printf("FLT_EPSILON=%g\n",m);

	float n=1;
	while(1+n!=1){n/=2;} n*=2;
	printf("float epsilon while=%g\n",n);

	float o=1;
	do {o/=2;}
	while(1+o!=1);
	o*=2;
	printf("float epsilon do while=%g\n",o);

	float p=1;
	for(p=1; 1+p!=1; p/=2){} p*=2;
	printf("float epsilon for=%g\n",p);

	long double q=LDBL_EPSILON;
	printf("LBDL_EPSILON=%Lg\n",q);

	long double r=1;
	while(1+r!=1){r/=2;} r*=2;
	printf("long double epsilon while=%Lg\n",r);

	long double s=1;
	do {s/=2;}
	while(1+s!=1);
	s*=2;
	printf("long double epsilon do while=%Lg\n",s);

	long double t=1;
	for(t=1; 1+t!=1; t/=2){} t*=2;
	printf("long double epsilon for=%Lg\n",t);


//Opgave II
	int max= INT_MAX/3;
	int bb=1;
	float sum = 0.0;
	while(bb<=max)
		{bb++, sum = sum+1.0f/bb;}
	printf("Sum = %g\n",sum);
	
	int ce=0;
	float sum2 = 0.0;
	while(ce<max-1){ce++,sum2=sum2+1.0f/(max-ce);}
	printf("Sum2 = %g\n",sum2+1.0f);

	int epsilon3 = equal(1.0,1.0,.1,.1);
	printf("Equal: %i\n",epsilon3);
}
