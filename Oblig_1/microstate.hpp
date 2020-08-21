#ifndef MICROSTATE_HPP
#define MICROSTATE_HPP

class microstate {
private:
 int m_N, m_M;

public:
  void Initialize(int M ,int N, int seed);
  void Calculate(int M, int N);
  void Print();
  int prob_function(float x,float mean_S, float sigma);
};

#endif
