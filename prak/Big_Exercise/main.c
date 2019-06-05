#include<stdlib.h>
#include<stdio.h>
#include<gsl/gsl_matrix.h>
#include<gsl/gsl_blas.h>
#define RND ((double)rand()/RAND_MAX)
#define FMT "%7.3f"
#define max_print 52

int jacobi(gsl_matrix*A,gsl_vector*e,gsl_matrix*V);

void matrix_print(gsl_matrix *A){
	for(int r=0;r<A->size1;r++){
		for(int c=0;c<A->size2;c++)fprintf(stderr,FMT,gsl_matrix_get(A,r,c));
		fprintf(stderr,"\n");}}

void vector_print(gsl_vector *v){
	for(int i=0;i<v->size;i++) fprintf(stderr,FMT,gsl_vector_get(v,i));
	fprintf(stderr,"\n");
	}

double coolshit(int ib) {
    int n= ib;
    double largest = 0;

    gsl_matrix *A = gsl_matrix_alloc(n,n);
    gsl_matrix *B = gsl_matrix_alloc(n,n);
    for(int i=0;i<n;i++) for(int j=i;j<n;j++) {
        double x = RND;
        gsl_matrix_set(A,i,j,x);
        gsl_matrix_set(A,j,i,x); //sets the i-j-th index of the matrix to be X, and the same for the j-i-th index (so the matrix is symmetric)
        }
    gsl_matrix_memcpy(B,A); //copies the insides of matrix A, into B
    //matrix_print(A);

    gsl_matrix *V = gsl_matrix_alloc(n,n);
    gsl_vector *e = gsl_vector_alloc(n);
    jacobi(A,e,V); //printf("n=%i, sweeps=%i\n",n,sweeps);

    if(n<max_print){
    largest =  gsl_vector_get(e,0);
    for(int i=0; i<n; i++){
        if( gsl_vector_get(e, i) > largest) {
            largest = gsl_vector_get(e, i);
        }
        else{largest = largest;}    
    }

    gsl_blas_dgemm(CblasNoTrans,CblasNoTrans,1,B,V,0,A);
    gsl_blas_dgemm(CblasTrans  ,CblasNoTrans,1,V,A,0,B);
    }
    return largest;
}

#define REAL double
inline static REAL sqr(REAL x) {return x*x;}
int linreg(int n, const REAL x[], const REAL y[], REAL* m, REAL* b, REAL* r){
    REAL   sumx = 0.0;                      /* sum of x     */
    REAL   sumx2 = 0.0;                     /* sum of x**2  */
    REAL   sumxy = 0.0;                     /* sum of x * y */
    REAL   sumy = 0.0;                      /* sum of y     */
    REAL   sumy2 = 0.0;                     /* sum of y**2  */

    for (int i=0;i<n;i++){ 
        sumx  += x[i];       
        sumx2 += sqr(x[i]);  
        sumxy += x[i] * y[i];
        sumy  += y[i];      
        sumy2 += sqr(y[i]); } 
    REAL denom = (n * sumx2 - sqr(sumx));
    if (denom == 0) {
        // singular matrix. can't solve the problem.
        *m = 0;
        *b = 0;
        if (r) *r = 0;
            return 1;}
    *m = (n * sumxy  -  sumx * sumy) / denom;
    *b = (sumy * sumx2  -  sumx * sumxy) / denom;
    if (r!=NULL) {
        *r = (sumxy - sumx * sumy / n) /    /* compute correlation coeff */
              sqr((sumx2 - sqr(sumx)/n) *
              (sumy2 - sqr(sumy)/n));}
    return 0; }


int main(int argc, char** argv){
    
    int n = (argc>1? atoi(argv[1]):5);
    double x [n];
    double y [n];

    for(int i=1; i<n+1; i++) {
        double eign = coolshit(i);
        //printf("%d  %g\n" , i, eign);
        x[i] = i;
        y[i] = eign;
    }

    REAL a,b,r;
        linreg(n,x,y,&a,&b,&r);
        for(int i=1; i<n+1; i++){
            printf("%g  %g  %g  %g\n",x[i], y[i], a, b); //x is N-size, y is largest eigenvalue, a is slope og the fit, and b is crosspoint with y-axis of the fit  
        }

    return 0;
}