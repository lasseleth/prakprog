#include<gsl/gsl_odeiv2.h>
#include<gsl/gsl_errno.h>
#include<stdio.h>
#include<math.h>
#include<gsl/gsl_matrix.h>
#define STEPPER gsl_odeiv2_step_rkf45
#define ABSERR 1e-6
#define RELERR 1e-6
#define STARTSTEP 1e-3

int hydro_diff(double r, const double y[], double dydr[], void* params){
	
    double e = *(double*)params;

	dydr[0]=y[1];
	
    dydr[1]= 2*(-1/r-e)*y[0];
    
    return GSL_SUCCESS;
}

double Aux(double e, double r){
    
    double rmin = 1e-3;

	gsl_odeiv2_system hydro_system;
	hydro_system.function = hydro_diff;
	hydro_system.jacobian = NULL;
	hydro_system.dimension = 2;
	hydro_system.params = (void*)&e;

	gsl_odeiv2_driver* hydro_driver = 
		gsl_odeiv2_driver_alloc_y_new (&hydro_system, STEPPER, STARTSTEP, ABSERR, RELERR);

	double t=rmin, y[2] = {t-t*t, 1-2*t};
	int status = gsl_odeiv2_driver_apply (hydro_driver, &t, r, y);
	if (status != GSL_SUCCESS) fprintf (stderr,"Fe: odeiv2 error: %d\n", status);

	gsl_odeiv2_driver_free (hydro_driver);
	return y[0];
}