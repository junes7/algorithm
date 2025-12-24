#include <iostream>
#include <map>
#include <algorithm>
using namespace std;
int main(void) {
    int n,rlt=0;
    double bn=0;
    string st,tar="ABC";
    map<char,int> grade={{'A',4},{'B',3},{'C',2},{'D',1},{'E',0}};
    cin>>n;
    for(int i=0;i<n;i++) {
        cin>>st;
        rlt+=grade[st[0]];
        if(tar.find(st[0])!=string::npos) {
            if(st[1]=='1')
                bn+=0.05;
            else if(st[1]=='2')
                bn+=0.025;
        }
    }
    cout<<fixed;
    cout.precision(6);
    cout<<(double)rlt/n+bn;
    return 0;
}