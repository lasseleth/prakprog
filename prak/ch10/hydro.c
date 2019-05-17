#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<gsl/gsl_multiroots.h>
#include<gsl/gsl_errno.h>
#include<gsl/gsl_vector.h>

double Aux(double e, double r);

int master(const gsl_vector *x, void *params, gsl_vector *f){

    double e=gsl_vector_get(x,0);

	  const double rmax=8.0;
	
    double fval=Aux(e,rmax);
	
    gsl_vector_set(f,0,fval);

	return GSL_SUCCESS;
}

int main(){
  const gsl_multiroot_fsolver_type *T;
  gsl_multiroot_fsolver *s;

  int status;
  size_t iter = 0;

  const size_t n = 1;

  gsl_multiroot_function func = {&master, n, NULL};

  double x_init[2] = {-10.5};

  gsl_vector *x = gsl_vector_alloc(n);

  gsl_vector_set (x, 0, x_init[0]);

  T = gsl_multiroot_fsolver_hybrids;
  s = gsl_multiroot_fsolver_alloc (T, 1);
  gsl_multiroot_fsolver_set(s,&func,x);

  do
    {
      iter++;
      status = gsl_multiroot_fsolver_iterate (s);

      if (status)
        break;

      printf("iteration=%i\tx=%g,\tfval=%g\n",iter,gsl_vector_get(s->x,0),gsl_vector_get(s->f,0));
      
      status = gsl_multiroot_test_residual (s->f, 1e-7);
    }
  while (status == GSL_CONTINUE && iter < 1000);

printf("Root found\niteration=%i\tx=%g,\tfval=%g\n",iter,gsl_vector_get(s->x,0),gsl_vector_get(s->f,0));

 
int i_points = 100;
double rmax = 8.0;
FILE *DATA = fopen("plot.txt","w");

for (int i = 1; i<i_points; i++)
{
	double r = rmax*i/i_points;
	double fvalue=Aux(gsl_vector_get(s->x,0),r);
	fprintf(DATA,"%g\t%g\n",r,fvalue);
}

  gsl_vector_free (x);
  gsl_multiroot_fsolver_free (s);

return 0;
}