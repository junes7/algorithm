#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(void) {
    int n;
    cin>>n;
    vector<int> arr(n);
    for(int i=0;i<n;i++)
        cin>>arr[i];
    if(*min_element(arr.begin(),arr.end())==arr[0])
        cout<<"ez";
    else if(*max_element(arr.begin(),arr.end())==arr[0])
        cout<<"hard";
    else
        cout<<"?";
    return 0;
}