#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<assert.h>
#include"params.h"

void* shoot(void* prms){
	params* args =(params*)prms;
	
	int n = params_get_throws(args);
	int* y_n = params_get_yn(args);
	unsigned int* seed = params_get_seed(args);

	double x,y;

	for(int i=0; i<n; i++){
		x = (double)rand_r(seed)/RAND_MAX;
		y = (double)rand_r(seed)/RAND_MAX;

		if( (x-0.5)*(x-0.5) + (y-0.5)*(y-0.5) <= 0.5*0.5){
			y_n[0]++;
		}
		else{
			y_n[1]++;
		}
	}
	
return NULL;
}