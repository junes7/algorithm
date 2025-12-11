#include <iostream>
using namespace std;
int main(void) {
    int x,y;
    while(1) {
        cin>>x>>y;
        if(x==0 && y==0) break;
        if(x+y==13)
            cout<<"Never speak again.\n";
        else {
            if(x>y) cout<<"To the convention.\n";
            else if(x<y) cout<<"Left beehind.\n";
            else cout<<"Undecided.\n";
        }
    }
    return 0;
}