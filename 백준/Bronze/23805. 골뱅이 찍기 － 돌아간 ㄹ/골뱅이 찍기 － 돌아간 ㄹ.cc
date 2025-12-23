#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    int n;
    cin>>n;
    vector<string> st(n*5);
    for(int i=0;i<n*5;i++) {
        if(i<n) {
            for(int j=0;j<n*3;j++)
                st[i]+="@";
            for(int j=0;j<n;j++)
                st[i]+=" ";
            for(int j=0;j<n;j++)
                st[i]+="@";
        } else if(n<=i && i<n*5-n) {
            for(int j=0;j<5;j++) {
                for(int k=0;k<n;k++)
                    st[i]+=j%2==0?"@":" ";
            }
        } else {
            for(int j=0;j<n;j++)
                st[i]+="@";
            for(int j=0;j<n;j++)
                st[i]+=" ";
            for(int j=0;j<n*3;j++)
                st[i]+="@";
        }
    }
    for(int i=0;i<n*5;i++)
        cout<<st[i]<<"\n";
    return 0;
}