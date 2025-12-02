#include <iostream>
#include <cmath>
using namespace std;
int main(void) {
    long n,m,s;
    cin>>n>>m>>s;
    cout<<min(s*m,(long)(s*(m+1)*(100-n)/100.0));
    return 0;
}