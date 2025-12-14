#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    int n,sumn;
    cin>>n;
    vector<int> arr(n);
    for(int i=0;i<n;i++) {
        cin>>arr[i];
        sumn+=arr[i];
    }
    if(n==0)
        cout<<"divide by zero";
    else {
        cout<<fixed;
        cout.precision(2);
        cout<<(double)sumn/n/(sumn/n);
    }
    return 0;
}