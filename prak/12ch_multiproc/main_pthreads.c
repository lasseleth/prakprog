#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<time.h>
#include"params.h"

void* shoot(void* prms);

int main(void){
	printf("First doing multi-threaded processing using pthreads.\n\n");
	/*make parameters*/
	int n = 5e7; /*throws*/
	int x[2];    /*succes/fail parameters*/
	int y[2];
	for(int i=0; i<2; i++){x[i] = 0;y[i] = 0;}
	time_t t; /*use current time as a seed*/
	t = time(NULL);
	unsigned int* seed = (unsigned int*)&t;

	
	/*setting parameters*/
	params prms,prms1;
	params_set(&prms, n, x, seed);
	params_set(&prms1, n, y, seed+1);

	/*making a thread and running shoots*/
	pthread_t thread;
	pthread_create(	&thread,NULL,
			shoot,(void*)&prms);

	shoot((void*)&prms1);
	pthread_join(thread,NULL);

	int *yn1 = params_get_yn(&prms);
	int *yn2 = params_get_yn(&prms1);
	
	int yes = yn1[0] +yn2[0]; 
	int total = yn1[0] + yn1[1] + yn2[0] + yn2[1];

	printf("Using two threads, pi has been estimated by throwing a total of %g darts at a 1x1 square with a r=0.5 circle inscribed inside.\n",(double)total);

	printf("The estimated pi is pi=%g\n\n",4*(double)yes/total);
return 0;
}







