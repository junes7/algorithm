#include <iostream>
using namespace std;
int main(void) {
    int t,n;
    string rlt;
    cin>>t;
    for(int i=0;i<t;i++) {
        cin>>n;
        rlt="Round 1";
        if(n<=25)
            rlt="World Finals";
        else if(n<=1000)
            rlt="Round 3";
        else if(n<=4500)
            rlt="Round 2";
        cout<<"Case #"<<i+1<<": "<<rlt<<"\n";
    }
    return 0;
}