#include <iostream>
using namespace std;
int main(void) {
    int m,d;
    cin>>m>>d;
    cout<<d/m+(d%m==0?0:1);
    return 0;
}