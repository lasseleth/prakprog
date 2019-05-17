#include"params.h"

void params_set(params* param, int throws, int* yes_no, unsigned int* seed){
	(*param).throws = throws;
	(*param).yes_no = yes_no;
	(*param).seed = seed;
return;
}

int params_get_throws(params* param){
	return (*param).throws;
}

int* params_get_yn(params* param){
	return (*param).yes_no;
}

unsigned int * params_get_seed(params* param){
	return (*param).seed;
}
