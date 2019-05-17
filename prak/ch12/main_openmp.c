#include<stdio.h>
#include<stdlib.h>
#include"params.h"
#include<time.h>


void* shoot(void* prms);

int main(void){
	printf("\nNow doing the same but with the OpenMP protocols instead.\n\n");
	int throws = 5e7;
       	int x[2];
	int y[2];	
	for(int i=0; i<2; i++){x[i]=0;y[i]=0;}
	time_t t; /*use current time as a seed*/
        t = time(NULL);
        unsigned int* seed = (unsigned int*)&t;

	params prms, prms1;
	params_set(&prms, throws, x, seed);
	params_set(&prms1, throws, y, seed+1);

#pragma omp parallel sections
	{
	#pragma omp section
		{
		shoot((void*)&prms);
		}
	#pragma omp section
		{
		shoot((void*)&prms1);
		}
	}

	int* yn1 = params_get_yn(&prms);
	int* yn2 = params_get_yn(&prms1);
	int yes = yn1[0] + yn2[0];
	int total = yn1[0] + yn1[1] + yn2[0] + yn2[1];

	printf("In total, %g darts were thrown using OpenMP multi-threading.\n",(double)total);
	printf("Pi was estimated to be pi=%g.\n",4*(double)yes/total);

	return 0;
}
