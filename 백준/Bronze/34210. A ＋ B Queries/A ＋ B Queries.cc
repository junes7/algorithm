#include "aplusb.h"

std::vector<int> global_A,global_B;
void initialize(std::vector<int> A, std::vector<int> B) {
  global_A=A;
  global_B=B;
  return;
}

int answer_question(int i, int j) {
  return global_A[i]+global_B[j];
}
