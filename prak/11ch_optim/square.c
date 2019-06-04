#include<gsl/gsl_multimin.h>
#include<assert.h>
#include<gsl/gsl_vector.h>
#include<math.h>
#include<gsl/gsl_errno.h>
#include<stdio.h>

struct experimental_data {int n; double *t,*y,*e;};

double least_squares(const gsl_vector *x, void *params) {
	double A=gsl_vector_get(x,0);
	double T=gsl_vector_get(x,1);
	double B=gsl_vector_get(x,2);

	struct experimental_data *p = (struct experimental_data*) params;
	int     n=p->n;
	double *t=p->t;
	double *y=p->y;
	double *e=p->e;
	double sum=0;
	#define MODEL(t) A*exp(-(t)/T)+B
	for(int i=0;i<n;i++){sum+=pow( (MODEL(t[i]) - y[i]) /e[i] ,2);}
	return sum;
}

int main(){

    double t[]= {0.47,1.41,2.36,3.30,4.24,5.18,6.13,7.07,8.01,8.95};
    double y[]= {5.49,4.08,3.54,2.61,2.09,1.91,1.55,1.47,1.45,1.25};
    double e[]= {0.26,0.12,0.27,0.10,0.15,0.11,0.13,0.07,0.15,0.09};

	int n=sizeof(t)/sizeof(t[0]);

	struct experimental_data params;
	params.n=n;
	params.t=t;
	params.y=y;
	params.e=e;

	gsl_multimin_function LS_func;
	LS_func.f=least_squares;
	LS_func.n=3;
	LS_func.params=(void*)&params;

	gsl_vector *x = gsl_vector_alloc(LS_func.n);
	gsl_vector_set(x,0,10);
	gsl_vector_set(x,1,10);
	gsl_vector_set(x,2,10);

	gsl_vector *step = gsl_vector_alloc(LS_func.n);
	gsl_vector_set(step,0,2);
	gsl_vector_set(step,1,2);
	gsl_vector_set(step,2,2);

	gsl_multimin_fminimizer *state =
		gsl_multimin_fminimizer_alloc(gsl_multimin_fminimizer_nmsimplex2,LS_func.n);
	gsl_multimin_fminimizer_set (state,&LS_func, x, step);

	int iter=0, status;
	do{
		iter++;
        double size = gsl_multimin_fminimizer_size(state);
		status = gsl_multimin_fminimizer_iterate(state);
		if(status){
            break;
			}

		status = gsl_multimin_test_size(size,1e-3);
        
        printf("iteration=%i\tx=%g,\ty=%g,\tz=%g,\tfval=%g\n",iter,gsl_vector_get(state->x,0),gsl_vector_get(state->x,1),gsl_vector_get(state->x,2),gsl_multimin_fminimizer_minimum(state));
      
		if( status == GSL_SUCCESS ) 
        {fprintf(stderr,"converged\n");
		printf ("Minimum at\n");

        printf("iteration=%i\tx=%g,\ty=%g,\tz=%g,\tfval=%g\n",iter,gsl_vector_get(state->x,0),gsl_vector_get(state->x,1),gsl_vector_get(state->x,2),gsl_multimin_fminimizer_minimum(state));
        }

	}while( status == GSL_CONTINUE && iter < 1000);

int i_points = 100;
double tmax = 9.5;
FILE *DATA = fopen("plot.txt","w");

for (int i = 1; i<i_points; i++)
{
    double A=gsl_vector_get(state->x,0);
    double T=gsl_vector_get(state->x,1);
    double B=gsl_vector_get(state->x,2);
    double t = tmax*i/i_points+0.5;
	double fvalue=A*exp(-(t)/T)+B;
	fprintf(DATA,"%g\t%g\n",t,fvalue);
}

gsl_multimin_fminimizer_free(state);
gsl_vector_free(x);
gsl_vector_free(step);

return 0;
}