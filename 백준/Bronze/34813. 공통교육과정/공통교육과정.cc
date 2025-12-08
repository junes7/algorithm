#include <iostream>
#include <map>
using namespace std;
int main(void) {
    string st;
    cin>>st;
    map<char,string> rlt={{'F',"Foundation"},
    {'C',"Claves"},{'V',"Veritas"},{'E',"Exploration"}};
    cout<<rlt[st[0]];
    return 0;
}