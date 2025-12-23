#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(void) {
    int n;
    string st,tar="uospc";
    cin>>n>>st;
    vector<int> arr(5);
    for(int i=0;i<tar.size();i++)
        arr[i]=count(st.begin(),st.end(),tar[i]);
    cout<<*min_element(arr.begin(),arr.end());
    return 0;
}