#include <iostream>
using namespace std;
int main(void) {
    int n,k;
    cin>>n>>k;
    for(int i=0;i<n-1;i++)
        k/=2;
    cout<<k;
    return 0;
}