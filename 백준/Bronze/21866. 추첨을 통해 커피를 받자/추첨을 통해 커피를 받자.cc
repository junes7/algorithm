#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    vector<int> arr(9),maxn={100,100,200,200,300,300,400,400,500};
    int hac=0,total=0;
    for(int i=0;i<9;i++) {
        cin>>arr[i];
        if(arr[i]>maxn[i]) {
            hac=1;
            break;
        }
        total+=arr[i];
    }
    cout<<(hac?"hacker":(total>=100?"draw":"none"));
    return 0;
}