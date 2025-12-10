#include <iostream>
using namespace std;
int main(void) {
    int s;
    double d,t;
    cin>>s>>d>>t;
    cout<<(d/(s*5280/3600)<=t?"MADE IT":"FAILED TEST");
    return 0;
}