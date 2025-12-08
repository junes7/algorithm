#include <iostream>
using namespace std;
int main(void) {
    int y,c,p;
    cin>>y>>c>>p;
    cout<<min(min(y/1,c/2),p/1);
    return 0;
}