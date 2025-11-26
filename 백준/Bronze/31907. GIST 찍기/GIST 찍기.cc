#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    int n;
    cin>>n;
    vector<string> p_list={"G...",".I.T","..S."};
    string str;
    for(int i=0;i<p_list.size();i++) {
        str="";
        for(int j=0;j<p_list[i].length();j++) {
            for(int k=0;k<n;k++) {
                str+=p_list[i][j];
            }
        }
        for(int j=0;j<n;j++) {
            cout<<str<<"\n";
        }
    }
    return 0;
}