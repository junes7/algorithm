#include <iostream>
#include <cmath>
using namespace std;
int main(void) {
    int l;
    cin>>l;
    cout<<fixed;
    cout.precision(9);
    cout<<0.5*l*l*sin(120*M_PI/180);
    return 0;
}