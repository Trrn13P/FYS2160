#include "microstate.hpp"
#include <iostream>
#include <cmath>
#include <random>
#include "armadillo"


using namespace std;
using namespace arma;


void microstate :: Initialize(int M ,int N,int seed)
{
  m_N = N;
  m_M = M;

  srand(seed);


}



int random_number;
int rnd_choices[2] = {-1,1};

void microstate :: Calculate(int M, int N){

int a_S[m_M];
//initiazing array
for(int i=0; i< M; i++){
    a_S[i] = 0;
}

//Calculating S for each microstate
for (int j=0; j < M; j++){
    for(int i=0; i < N;i++){
      random_number = rand()%2;
      a_S[j] += (rnd_choices[random_number]);
    }
}

float mean_S;
for (int i=0; i<M; i++){
  mean_S += a_S[i];
}
mean_S = mean_S*(1./M);

float sigma;
float sum;
for (int i=0; i<M; i++){
  sum  += pow(a_S[i]-mean_S,2);
}

sigma = sqrt(1./(M-1) * sum);

mat h(1,M);
mat P(1,M);




float stepsize = (30+30)* 1./M;
stepsize = (30+30+stepsize)* 1./M;
float k = 0;
for(int i=0;i<M;i++){
    h(0,i) = -30 + stepsize * k;
    k += 1;
    //cout << h(0,i) << endl;
}





}

int microstate :: prob_function(float x, float mean_S, float sigma){
  return 1./(sigma * sqrt(2*M_PI)) * exp(-pow(x-mean_S,2)/(2*pow(sigma,2)));
}



void microstate :: Print(){

}
