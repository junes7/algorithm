#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    int n;
    bool iskor=false;
    cin>>n;
    vector<string> arr(n);
    for(int i=0;i<n;i++) {
        cin>>arr[i];
        if(arr[i]=="korea")
            iskor=true;
        if(arr[i]=="yonsei") {
            cout<<(!iskor?"Yonsei Won!":"Yonsei Lost...");
            break;
        }
    }
    return 0;
}