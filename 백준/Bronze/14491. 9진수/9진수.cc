#include <iostream>
using namespace std;
string solve(string r,int n) {
    if(n==0)
        return r;
    return solve((n%9?to_string(n%9):"0")+r,n/9);
}
int main(void) {
    int n;
    cin>>n;
    cout<<solve("",n);
    return 0;
}