#include <iostream>
#include <sstream>
using namespace std;
int main(void) {
    string st1,st2;
    cin>>st1>>st2;
    int idx=0,t1[2],t2[2];
    stringstream ss1(st1);
    while(getline(ss1,st1,':'))
        t1[idx++]=stoi(st1);
    idx=0;
    stringstream ss2(st2);
    while(getline(ss2,st2,':'))
        t2[idx++]=stoi(st2);
    cout<<(t1[0]*60+t1[1]<t2[0]*60+t2[1]?"YES":"NO");
    return 0;
}