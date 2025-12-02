#include <iostream>
using namespace std;
int main(void) {
    long n,m,s;
    cin>>n>>m>>s;
    cout<<min(s*m,s*(m+1)*(100-n)/100);
    return 0;
}