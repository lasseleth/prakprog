#include<gsl/gsl_odeiv2.h>
#include<gsl/gsl_errno.h>

int ode_logistic( double x, const double y[], double dydt[], void * params){
	dydt[0] = y[0]*(1-y[0]);
	return GSL_SUCCESS;
}

double mylogistic( double x){
	gsl_odeiv2_system sys;
	sys.function = ode_logistic;
	sys.jacobian = NULL;
	sys.dimension = 1;
	sys.params = NULL;
	gsl_odeiv2_driver * driver;
	double hstart = 0.05, eps = 1e-9, tau = 1e-9;
	driver = gsl_odeiv2_driver_alloc_y_new(&sys,gsl_odeiv2_step_rkf45,hstart,eps,tau);
	double x0 = 0;
	double y[] = {0.5};

	gsl_odeiv2_driver_apply(driver, &x0, x, y);
	gsl_odeiv2_driver_free(driver);
	return y[0];
}
	