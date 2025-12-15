#include <iostream>
using namespace std;
int main(void) {
    int a,b;
    string c;
    cin>>a>>b>>c;
    if((c[c.length()-1]-48)%2)
        cout<<(a^b);
    else
        cout<<a;
    return 0;
}