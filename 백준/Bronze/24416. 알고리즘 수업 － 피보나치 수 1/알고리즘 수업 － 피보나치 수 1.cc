#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    int n;
    cin>>n;
    vector<int> fibo(n+1);
    fibo[1]=fibo[2]=1;
    for(int i=3;i<n+1;i++)
        fibo[i]=fibo[i-1]+fibo[i-2];
    cout<<fibo[n]<<' '<<n-2;
    return 0;
}