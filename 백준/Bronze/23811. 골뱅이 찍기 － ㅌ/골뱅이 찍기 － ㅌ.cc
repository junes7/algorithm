#include <iostream>
using namespace std;
int main(void) {
    int n;
    cin>>n;
    string st="";
    for(int i=0;i<5;i++) {
        for(int j=0;j<n;j++) {
            if(i%2==0)
                for(int k=0;k<5*n;k++)
                    st+="@";
            else
                for(int k=0;k<n;k++)
                    st+="@";
            st+="\n";
        }
    }
    cout<<st;
    return 0;
}