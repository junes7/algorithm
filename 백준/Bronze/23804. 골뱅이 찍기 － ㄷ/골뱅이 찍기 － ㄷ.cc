#include <iostream>
using namespace std;
int main(void) {
    int n;
    cin>>n;
    string st="";
    for(int i=0;i<n*5;i++) {
        if(i<n || i>=n*5-n)
            for(int j=0;j<n*5;j++)
                st+="@";
        else
            for(int j=0;j<n;j++)
                st+="@";
        st+="\n";
    }
    cout<<st;
    return 0;
}