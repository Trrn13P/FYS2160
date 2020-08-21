#include <iostream>
#include <cmath>

#include "microstate.hpp"

//#include "matplotlibcpp.h"

using namespace std;




int main(int argc, char const *argv[]) {

  //Parameters
  int N = 60;
  int M = 1E4;
  int seed = 2;

  //Solver integral
  microstate my_solver;
  my_solver.Initialize(M,N, seed);
  my_solver.Calculate(M,N);
  my_solver.Print();

  return 0;
}
