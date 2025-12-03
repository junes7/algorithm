#include <iostream>
using namespace std;
int main(void) {
    int n,elem;
    bool rlt=true;
    cin>>n;
    for(int i=0;i<n;i++) {
        cin>>elem;
        if(elem<48) {
            rlt=false;
            break;
        }
    }
    cout<<(rlt?"True":"False");
    return 0;
}