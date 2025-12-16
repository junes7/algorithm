#include <iostream>
#include <cmath>
using namespace std;
int main(void) {
    int a,b,n;
    while(1) {
        cin>>b>>n;
        if(b==0 && n==0) break;
        a=1;
        while(pow(a,n)<b)
            a+=1;
        cout<<(pow(a,n)-b<b-pow(a-1,n)?a:a-1)<<"\n";
    }
    return 0;
}