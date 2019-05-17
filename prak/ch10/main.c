#include<stdio.h>
#include<math.h>
#include<gsl/gsl_multiroots.h>
#include<gsl/gsl_errno.h>
#include<gsl/gsl_vector.h>

int rosenbrock(const gsl_vector *x, void *params, gsl_vector *f){
	
  double a=gsl_vector_get(x,0);
	double b=gsl_vector_get(x,1);

	double dfda=2*(a-1)-400*(b*a-a*a*a);
	double dfdb=200*(b-a*a);

	gsl_vector_set(f,0,dfda);
	gsl_vector_set(f,1,dfdb);

    return GSL_SUCCESS;
    
}

int main (){
  const gsl_multiroot_fsolver_type *T;
  gsl_multiroot_fsolver *s;

  int status;
  size_t iter = 0;

  const size_t n = 2;

  gsl_multiroot_function func = {&rosenbrock, n, NULL};

  double x_init[2] = {1.5, 1.5};

  gsl_vector *x = gsl_vector_alloc(n);

  gsl_vector_set (x, 0, x_init[0]);
  gsl_vector_set (x, 1, x_init[1]);

  T = gsl_multiroot_fsolver_hybrids;
  s = gsl_multiroot_fsolver_alloc (T, 2);
  gsl_multiroot_fsolver_set(s,&func,x);

  do
    {
      iter++;
      status = gsl_multiroot_fsolver_iterate (s);

      if (status)
        break;

      printf("iteration=%i\tx=%g,\ty=%g,\tfval=%g\n",iter,gsl_vector_get(s->x,0),gsl_vector_get(s->x,1),gsl_vector_get(s->f,0));
      
      status = gsl_multiroot_test_residual (s->f, 1e-7);
    }
  while (status == GSL_CONTINUE && iter < 1000);

printf("Root found\niteration=%i\tx=%g,\ty=%g,\tfval=%g\n",iter,gsl_vector_get(s->x,0),gsl_vector_get(s->x,1),gsl_vector_get(s->f,0));
  gsl_vector_free (x);
  gsl_multiroot_fsolver_free (s);
 
  return 0;
}