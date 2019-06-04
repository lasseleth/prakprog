#include<stdio.h>
#include<math.h>
#include<gsl/gsl_multimin.h>
#include<gsl/gsl_errno.h>
#include<gsl/gsl_vector.h>

double rosenbrock(const gsl_vector *x, void *params){
	
    double a=gsl_vector_get(x,0);
	  double b=gsl_vector_get(x,1);

    double func=pow((1-a),2)+pow(100*(b-pow(a,2)),2);

    return func;
}
int 
main(void){
  const gsl_multimin_fminimizer_type *T = 
    gsl_multimin_fminimizer_nmsimplex2;
  gsl_multimin_fminimizer *s = NULL;
  

  size_t iter = 0;
  int status;

  gsl_vector *x;
  x = gsl_vector_alloc (2);
  gsl_vector_set (x, 0, 5.0);
  gsl_vector_set (x, 1, 5.0);

  gsl_vector *ss;
  ss = gsl_vector_alloc (2);
  gsl_vector_set_all (ss, 1.0);

  gsl_multimin_function rosen_func;
  rosen_func.n = 2;
  rosen_func.f = rosenbrock;
  
  s = gsl_multimin_fminimizer_alloc (T, 2);
  gsl_multimin_fminimizer_set (s, &rosen_func, x, ss);

  do
    {
      iter++;
      status = gsl_multimin_fminimizer_iterate(s);
      
      if (status) 
        {break;}

      double size = gsl_multimin_fminimizer_size (s);
      status = gsl_multimin_test_size (size, 1e-4);
      printf("iteration=%i\tx=%g,\ty=%g,\tfval=%g\n",iter,gsl_vector_get(s->x,0),gsl_vector_get(s->x,1),gsl_multimin_fminimizer_minimum(s));
      

      if (status == GSL_SUCCESS)
        {printf ("converged to minimum at\n");

        printf("iteration=%i\tx=%g,\ty=%g,\tfval=%g\n",iter,gsl_vector_get(s->x,0),gsl_vector_get(s->x,1),gsl_multimin_fminimizer_minimum(s));
        }
    }
  while (status == GSL_CONTINUE && iter < 1000);
  
  gsl_vector_free(x);
  gsl_vector_free(ss);
  gsl_multimin_fminimizer_free (s);

  return status;
}