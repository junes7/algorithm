#include <iostream>
using namespace std;
int main(void) {
    int m,seed,x1,x2,a,c;
    cin>>m>>seed>>x1>>x2;
    for(int a=0;a<m;a++) {
        for(int c=0;c<m;c++) {
            if(x1==(a*seed+c)%m && x2==(a*x1+c)%m) {
                cout<<a<<' '<<c;
                return 0;
            }
        }
    }
}