#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(void) {
    int n,k;
    string tmp;
    cin>>n>>k;
    vector<int> arr(k);
    for(int i=0;i<k;i++) {
        tmp=to_string(n*(i+1));
        reverse(tmp.begin(), tmp.end());
        arr[i]=stoi(tmp);
    }
    cout<<*max_element(arr.begin(),arr.end());
    return 0;
}