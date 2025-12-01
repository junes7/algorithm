#include <iostream>
#include <cmath>
using namespace std;
int main(void) {
    long n;
    cin>>n;
    cout<<((double)pow(n,2)/pow(10,8)>1?"Time limit exceeded":"Accepted");
    return 0;
}