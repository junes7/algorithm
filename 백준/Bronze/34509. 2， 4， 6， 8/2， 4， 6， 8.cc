#include <iostream>
#include <algorithm>
using namespace std;
int main(void) {
    string st,rev_st;
    for(int i=10;i<99;i++) {
        st=to_string(i);
        rev_st=to_string(i);
        reverse(rev_st.begin(),rev_st.end());
        if(st.find("8")==string::npos) {
            if((st[0]-48+st[1]-48)%6==0 && stoi(rev_st)%4==0) {
                cout<<st;
                break;
            }
        }
    }
    return 0;
}