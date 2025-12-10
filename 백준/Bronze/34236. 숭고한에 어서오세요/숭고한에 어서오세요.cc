#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    int n;
    cin>>n;
    vector<int> arr(n);
    for(int i=0;i<n;i++)
        cin>>arr[i];
    cout<<arr.back()+(arr[1]-arr[0]);
    return 0;
}