#include <iostream>
using namespace std;
int main(void) {
    int n;
    cin>>n;
    cout<<(n%4==0?"Even":(n%2==0?"Odd":"Either"));
    return 0;
}