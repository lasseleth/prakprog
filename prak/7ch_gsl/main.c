#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<gsl/gsl_linalg.h>
#include<gsl/gsl_blas.h>
#include<gsl/gsl_matrix.h>
#include<gsl/gsl_vector.h>

int main(){
/* Defining matrices */
gsl_matrix* M=gsl_matrix_alloc(3,3);
gsl_matrix_set(M,0,0,6.13);
gsl_matrix_set(M,0,1,-2.90);
gsl_matrix_set(M,0,2,5.86);

gsl_matrix_set(M,1,0,8.08);
gsl_matrix_set(M,1,1,-6.31);
gsl_matrix_set(M,1,2,-3.89);

gsl_matrix_set(M,2,0,-4.36);
gsl_matrix_set(M,2,1,1.00);
gsl_matrix_set(M,2,2,0.19);

gsl_vector* b=gsl_vector_alloc(3);
gsl_vector_set(b,0,6.23);
gsl_vector_set(b,1,5.37);
gsl_vector_set(b,2,2.29);

gsl_vector* x=gsl_vector_alloc(3);

gsl_matrix* A=gsl_matrix_alloc(3,3);
gsl_matrix_memcpy(A,M);

gsl_linalg_HH_solve(M,b,x);

printf("x=\n");
gsl_vector_fprintf(stdout,x,"%g");

gsl_vector* ny_b=gsl_vector_alloc(3);
gsl_blas_dgemv(CblasNoTrans,1.0,A,x,0.0,ny_b);
printf("ny_b=\n");
gsl_vector_fprintf(stdout,ny_b,"%g");

gsl_vector_free(b);
gsl_vector_free(x);
gsl_matrix_free(M);
gsl_matrix_free(A);

return 0;
}