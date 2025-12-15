#include <iostream>
#include <cmath>
using namespace std;
int main(void) {
    int t;
    double a,b;
    cin>>t;
    for(int i=0;i<t;i++) {
        cin>>a>>b;
        cout<<(int)pow(a/b,2)<<"\n";
    }
    return 0;
}