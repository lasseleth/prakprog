#include<stdio.h>
#include<gsl/gsl_sf_airy.h>
#include<math.h>

int main(){
        for(double x=-20;x<20;x+=0.2)
            printf("%g %g %g\n",x,gsl_sf_airy_Ai(x,GSL_PREC_APPROX),gsl_sf_airy_Bi(x,GSL_PREC_APPROX));
return 0;

}