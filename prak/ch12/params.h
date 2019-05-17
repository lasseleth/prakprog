#ifndef HAVE_PARAMS_H
#define HAVE_PARAMS_H
typedef struct parameters {
        int throws;
        int* yes_no;
        unsigned int* seed;
} params;

void params_set(params* param, int throws, int* yes_no, unsigned int* seed);

int params_get_throws(params* param);

int* params_get_yn(params* param);

unsigned int * params_get_seed(params* param);

#endif
