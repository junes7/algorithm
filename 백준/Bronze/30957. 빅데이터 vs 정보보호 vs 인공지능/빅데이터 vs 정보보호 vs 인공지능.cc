#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(void) {
    int n,maxn=0;
    string st,tar="BSA";
    cin>>n>>st;
    vector<int> arr(3);
    for(int i=0;i<tar.length();i++) {
        arr[i]=count(st.begin(),st.end(),tar[i]);
        if(maxn<arr[i]) maxn=arr[i];
    }
    st="";
    if(arr[0]==arr[1] && arr[1]==arr[2] && arr[0]==arr[2])
        st+="SCU";
    else {
        for(int i=0;i<arr.size();i++)
            if(arr[i]==maxn) st+=tar[i];
    }
    cout<<st;
    return 0;
}