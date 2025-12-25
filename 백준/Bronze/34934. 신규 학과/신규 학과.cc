#include <iostream>
using namespace std;
int main(void) {
    int n,yr;
    string sub;
    cin>>n;
    for(int i=0;i<n;i++) {
        cin>>sub>>yr;
        if(yr==2026) {
            cout<<sub;
            break;
        }
    }
    return 0;
}