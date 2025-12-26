#include <iostream>
using namespace std;
int main(void) {
    int n,d;
    string st;
    cin>>n>>d;
    for(int i=0;i<n;i++) {
        cin>>st;
        for(int j=0;j<st.size();j++) {
            if(st[j]=='d')
                st[j]=d==1?'q':'b';
            else if(st[j]=='b')
                st[j]=d==1?'p':'d';
            else if(st[j]=='q')
                st[j]=d==1?'d':'p';
            else
                st[j]=d==1?'b':'q';
        }
        cout<<st<<"\n";
    }
    return 0;
}