#include <iostream>
using namespace std;
int main(void) {
    int w1,h1,w2,h2;
    cin>>w1>>h1>>w2>>h2;
    cout<<4+max(w1,w2)*2+(h1+h2)*2;
    return 0;
}