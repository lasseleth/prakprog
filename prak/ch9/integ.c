#include<math.h>
#include<stdio.h>
#include<gsl/gsl_integration.h>
#include<gsl/gsl_errno.h>

double func(double x, void* params){
    double func = log(x)/sqrt(x);
    return func;
}

int main(){
	int limit = 1000;
	gsl_integration_workspace *w =
		gsl_integration_workspace_alloc(limit);
    
    double result, error;
	gsl_function F;
	F.function = &func;
	
	double epsrel=1e-6,epsabs=1e-6;

    gsl_integration_qags(&F,0.0,1.0,epsrel,epsabs,limit,w,&result,&error);

    fprintf(stdout,"Resultat=\t%1.4f\n",result);

    gsl_integration_workspace_free(w);
return 0;
}