#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(void) {
    int tar,idx;
    string rlt;
    vector<int> arr(50);
    for(int i=0;i<50;i++)
        cin>>arr[i];
    cin>>tar;
    idx=find(arr.begin(),arr.end(),tar)-arr.begin()+1;
    if(idx<=5)
        rlt="A+";
    else if(idx<=15)
        rlt="A0";
    else if(idx<=30)
        rlt="B+";
    else if(idx<=35)
        rlt="B0";
    else if(idx<=45)
        rlt="C+";
    else if(idx<=48)
        rlt="C0";
    else
        rlt="F";
    cout<<rlt;
    return 0;
}