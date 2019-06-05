#include<stdlib.h>
#include<stdio.h>
#include<gsl/gsl_matrix.h>
#include<gsl/gsl_blas.h>
#define RND ((double)rand()/RAND_MAX)
#define FMT "%7.3f"
#define max_print 11

int jacobi(gsl_matrix*A,gsl_vector*e,gsl_matrix*V);

void matrix_print(gsl_matrix *A){
	for(int r=0;r<A->size1;r++){
		for(int c=0;c<A->size2;c++)fprintf(stderr,FMT,gsl_matrix_get(A,r,c));
		fprintf(stderr,"\n");}}

void vector_print(gsl_vector *v){
	for(int i=0;i<v->size;i++) fprintf(stderr,FMT,gsl_vector_get(v,i));
	fprintf(stderr,"\n");
	}

int main(int argc, char** argv)
{
int n=(argc>1? atoi(argv[1]):5);

gsl_matrix *A = gsl_matrix_alloc(n,n);
gsl_matrix *B = gsl_matrix_alloc(n,n);
for(int i=0;i<n;i++) for(int j=i;j<n;j++) {
	double x = RND;
	gsl_matrix_set(A,i,j,x);
	gsl_matrix_set(A,j,i,x);
	}
gsl_matrix_memcpy(B,A);


gsl_matrix *V = gsl_matrix_alloc(n,n);
gsl_vector *e = gsl_vector_alloc(n);
int sweeps=jacobi(A,e,V); printf("n=%i, sweeps=%i\n",n,sweeps);


if(n<max_print){
fprintf(stderr,"\nRandom symmetric matrix A: \n"); matrix_print(B);
fprintf(stderr,"\nResult of Jacobi diagonalization: \n");
fprintf(stderr, "eigenvalues:\n");
vector_print(e);
double largest =  gsl_vector_get(e,0);
for(int i=0; i<n; i++){
    if( gsl_vector_get(e, i) > largest) {
        largest = gsl_vector_get(e, i);
    }
    else{largest = largest;}    
}
fprintf(stderr, "\nOf which %g is the largest\n\n" , largest);

gsl_blas_dgemm(CblasNoTrans,CblasNoTrans,1,B,V,0,A);
gsl_blas_dgemm(CblasTrans  ,CblasNoTrans,1,V,A,0,B);
//fprintf(stderr, "check: V^T*A*V should be diagonal with above eigenvalues:\n");
//matrix_print(B);
}
fprintf(stderr, "If you wish to change the size of the matrix, make clean and the type make n=>>value<<\n");
return 0;
}