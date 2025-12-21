#include <iostream>
using namespace std;
int main(void) {
    int a,b,c,d,s,e,mid,fit,rlt;
    while(true) {
        cin>>a>>b>>c>>d;
        if(a==0 && b==0 && c==0 && d==0) break;
        if(a<b) swap(a,b);
        if(c<d) swap(c,d);
        
        s=1,e=100;
        while(s<=e) {
            mid=(s+e)/2;
            fit=(a*mid>c*100||b*mid>d*100)?0:1;
            if(fit) {
                s=mid+1;
                rlt=mid;
            } else {
                e=mid-1;
            }
        }
        cout<<rlt<<"%\n";
    }
    return 0;
}