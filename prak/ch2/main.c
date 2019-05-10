#include<stdio.h>
#include<math.h>
#include<complex.h>

int main(){
	printf("Gamma(5)=%g\n",tgamma(5.0));
	printf("Bessel, J1(0.5)=%g\n",j1(0.5));
	
	double complex a = -2.0;
	double complex negSqrt = csqrt(-2.0);
	double pReal = creal(negSqrt);
	double pImag = cimag(negSqrt);

	printf("sqrt(%f)= %f + %f i", (float) a, pReal, pImag);
	printf("\n");
	/*ved (float) typecastes z til en float, i stedet for en double complex */

	double complex ei = cexp(I);
	double eireal = creal(ei);
	double eiimag = cimag(ei);
	printf("e^i=\%f+%f i\n",eireal, eiimag);
	
	/*_________________________________*/
	double complex epi = cexp(I*M_PI);
	double epireal = creal(epi);
	double epiimag = cimag(epi);
	printf("e^(pi*i) = %f+%f i\n", epireal,epiimag);

	
	/*_________________________________*/
	double complex ie = cpow(I,M_E);
	double iereal = creal(ie);
	double ieimag = cimag(ie);
	printf("i^e = %f %fi \n", iereal, ieimag);


	/*_________________________________*/
	float x = 0.1111111111111111111111111111;
	double y = 0.1111111111111111111111111111;
	long double z = 0.1111111111111111111111111111L;
	printf("float       = %.25g \n", x);
	printf("double      = %.25lg \n", y);
	printf("long double = %.25Lg \n", z);
return 0;
}
