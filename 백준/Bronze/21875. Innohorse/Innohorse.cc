#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    string a,b;
    cin>>a>>b;
    vector<int> rlt={abs(a[0]-b[0]),abs(a[1]-b[1])};
    cout<<(rlt[0]>rlt[1]?rlt[1]:rlt[0])<<' '<<(rlt[0]>rlt[1]?rlt[0]:rlt[1]);
    return 0;
}