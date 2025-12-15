#include <iostream>
using namespace std;
int main(void) {
    int n;
    cin>>n;
    cout<<(n%2==1?0:(n/2%2==0?2:1));
    return 0;
}