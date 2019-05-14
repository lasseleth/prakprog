#include<stdio.h>
#include<stdlib.h>
#include"nvector.h"

nvector* nvector_alloc(int n){
  nvector* v = malloc(sizeof(nvector));
  (*v).size = n;
  (*v).data = malloc(n*sizeof(double));
  if( v==NULL ) fprintf(stderr,"error in nvector_alloc\n");
  return v;
}
void nvector_free(nvector* v){ free(v->data); free(v);}
void nvector_set(nvector* v, int i, double value){ (*v).data[i]=value; }

double nvector_get(nvector* v, int i){return (*v).data[i]; }
double nvector_dot_product (nvector* u, nvector* v){

double result=0.0;
for (int i=0; i<(*v).size; i++){
	result +=(*v).data[i]*(*u).data[i];}
return result;
}
