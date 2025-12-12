#include <iostream>
#include <vector>
#include <map>
using namespace std;
int main(void) {
    string ps;
    vector<int> arr(2);
    map<char,int> rlt={{'k',0},{'p',1},{'n',3},{'b',3},{'r',5},{'q',9}};
    for(int i=0;i<8;i++) {
        cin>>ps;
        for(int j=0;j<8;j++) {
            if(ps[j]=='.')
                continue;
            else {
                if(ps[j]>=97)
                    arr[1]+=rlt[ps[j]];
                else
                    arr[0]+=rlt[ps[j]+32];
            }
        }
    }
    cout<<arr[0]-arr[1];
    return 0;
}