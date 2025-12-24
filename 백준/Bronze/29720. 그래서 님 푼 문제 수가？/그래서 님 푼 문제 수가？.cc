#include <iostream>
using namespace std;
int main(void) {
    int n,m,k;
    cin>>n>>m>>k;
    cout<<max(n-(m*k),0)<<' '<<n-m*(k-1)-1;
    return 0;
}