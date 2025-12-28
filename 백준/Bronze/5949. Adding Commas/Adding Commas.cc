#include <iostream>
#include <algorithm>
using namespace std;
int main(void) {
    int n,cnt=0;
    string st,rlt="";
    cin>>st;
    for(int i=st.size()-1;i>=0;i--) {
        if(cnt-3==0) {
            rlt+=',';
            cnt=0;
        }
        rlt+=st[i];
        cnt++;
    }
    reverse(rlt.begin(),rlt.end());
    cout<<rlt;
}