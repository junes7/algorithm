#include <iostream>
using namespace std;
int main(void) {
    int n,m;
    cin>>n>>m;
    cout<<n/m+(n%m==0?0:1);
    return 0;
}