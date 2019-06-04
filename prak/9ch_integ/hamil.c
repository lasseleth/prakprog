#include<math.h>
#include<stdio.h>
#include<gsl/gsl_integration.h>
#include<gsl/gsl_errno.h>

double haminteg(double x, void* params){
    double a = *(double*)params;
    double f = (-a*a*x*x/2 + a/2 + x*x/2)*exp(-a*x*x);
    return f;
}

double norminteg(double x, void* params){
    double a = *(double*)params;
    double f = exp(-a*x*x);
    return f;
}

int main(){
    double a_min=0.01, a_max=10.0, a_trin=1000;
    double a_trin_str=(a_max-a_min)/a_trin;
	
    for(double a = a_min; a<(a_max+a_trin_str);a+=a_trin_str){
    int limit = 1000;
	gsl_integration_workspace *w_ham =
		gsl_integration_workspace_alloc(limit);

	gsl_integration_workspace *w_norm =
		gsl_integration_workspace_alloc(limit);
    
    double ham_result, norm_result, ham_error, norm_error;

	gsl_function hamint;
	hamint.function = &haminteg;
    hamint.params = &a;

    gsl_function normint;
    normint.function = &norminteg;
	normint.params = &a;

	double epsrel=1e-6,epsabs=1e-6;

    gsl_integration_qagi(&hamint,epsrel,epsabs,limit,w_ham,&ham_result,&ham_error);
    gsl_integration_qagi(&normint,epsrel,epsabs,limit,w_norm,&norm_result,&norm_error);

    double result = ham_result/norm_result;

    printf("%g\t%g\n",a,result);

    gsl_integration_workspace_free(w_norm);
    gsl_integration_workspace_free(w_ham);
    }
return 0;
}