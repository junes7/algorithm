#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    vector<int> m(11);
    int n,b,s,rlt=0;
    float l;
    for(int i=0;i<11;i++)
        cin>>m[i];
    cin>>n;
    for(int i=0;i<n;i++) {
        cin>>b>>l>>s;
        if(l>=2.0 && s>=17)
            rlt+=m[b];
    }
    cout<<rlt;
    return 0;
}