#include <iostream>
using namespace std;
int main(void) {
    double d,w;
    int n;
    cin>>d>>w>>n;
    cout<<(n<=d/w*3.14159?"YES":"NO");
    return 0;
}