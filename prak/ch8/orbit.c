#include<stdio.h>
#include<math.h>
#include<getopt.h>
#include<gsl/gsl_errno.h>
#include<gsl/gsl_odeiv2.h>

int orbital_equation
(double phi, const double y[], double dydx[], void *params)
{
    double epsilon = *(double *) params;
    dydx[0] = y[1];
    dydx[1] = 1 - y[0] + epsilon * y[0] * y[0];
    return GSL_SUCCESS;
}

int main(int argc, char **argv) {
    double epsilon=0.0, dudx=0.0;

while (1){
	int opt = getopt(argc, argv, "e:p:");
	if( opt == -1 ) break;
	switch (opt) {
		case 'e': epsilon = atof (optarg); break;
		case 'p': dudx  = atof (optarg); break;
		default:
			fprintf (stderr, "Usage: %s --epsilon epsilon --uprime uprime\n", argv[0]);
			exit (EXIT_FAILURE);
		}
}

    gsl_odeiv2_system orbit;
	orbit.function = orbital_equation;
	orbit.jacobian = NULL;
	orbit.dimension = 2;
	orbit.params = (void *) &epsilon;

	double hstart = 1e-3, epsabs = 1e-6, epsrel = 1e-6;
	double phi_max = 60 * M_PI, delta_phi = 0.05;

	gsl_odeiv2_driver *driver =
		gsl_odeiv2_driver_alloc_y_new
			(&orbit, gsl_odeiv2_step_rk8pd, hstart, epsabs, epsrel);

	double t = 0, y[2] = { 1, dudx };
	for (double phi = 0; phi < phi_max; phi += delta_phi) {
		int status = gsl_odeiv2_driver_apply (driver, &t, phi, y);
		printf ("%g %g\n", phi, y[0]);
		if (status != GSL_SUCCESS) fprintf (stderr, "fun: status=%i", status);
		}

	gsl_odeiv2_driver_free (driver);
return EXIT_SUCCESS;
}