#include<stdio.h>
#include<math.h>
#include<gsl/gsl_errno.h>
#include<gsl/gsl_odeiv2.h>

int diff_equation
(double x, const double y[], double dydx[], void *params){
    dydx[0]=y[0]*(1-y[0]);
return GSL_SUCCESS;
}

double log(double x){
	gsl_odeiv2_system diff;
	diff.function = diff_equation;
	diff.jacobian = NULL;
	diff.dimension = 2;
	diff.params = NULL;

	double hstart = 1e-3, epsabs = 1e-6, epsrel = 1e-6;

	gsl_odeiv2_driver *driver =
		gsl_odeiv2_driver_alloc_y_new
			(&diff, gsl_odeiv2_step_rkf45, hstart, epsabs, epsrel);

	double t = 0;
    double y[1] = {0.5};
	gsl_odeiv2_driver_apply (driver,&t,x,y);

	gsl_odeiv2_driver_free (driver);
return y[0];
}

int main(){
    for(double x=0; x<=3;x+=0.1)
        printf("%g %g\n",x,log(x));

return 0;
}