#include "nvector.h"
#include "stdio.h"
#include "stdlib.h"
#include "math.h"
#define RND (double)rand()/RAND_MAX

int main(){
	int n = 5;
	printf("\nmain: testing nvector_alloc\n");
	nvector *v = nvector_alloc(n);
	if (v == NULL) printf("test failed\n");
	else printf("test passed\n");

	printf("\nmain: testing nvector_set and nvector_get\n");
	double value = RND;
	int i = n / 2;
	nvector_set(v, i, value);
	double vi = nvector_get(v, i);
	if (vi==value) printf("test passed\n");
	else printf("test failed\n");

	nvector_free(v);
	int j;
	nvector *a=nvector_alloc(n);
	double k=5.0;
	for (j=0; j<n; j++){nvector_set(a,j,k);}

	int h;
	nvector *b=nvector_alloc(n);
        double l=5.0;
	for (h=0; h<n; h++){nvector_set(b,h,l);}

	double dot = nvector_dot_product(a,b);
	printf("value of dot=%g\n",dot);

	printf("testing nvector_dot_product\n");
	double rigtig=125;
	if (dot == rigtig) printf("test passed\n");
        else printf("test failed\n");

	nvector_free(a);
	nvector_free(b);
	return 0;
}
