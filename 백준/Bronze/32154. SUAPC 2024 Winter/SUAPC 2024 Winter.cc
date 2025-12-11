#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    int n,l;
    cin>>n;
    vector<vector<int>> rlt={
        {1,2,3,4,5,6,7,8,10,12,13},
        {1,3,5,6,7,8,9,12,13},
        {1,3,5,6,7,8,9,12,13},
        {1,2,3,5,6,7,8,12,13},
        {1,3,5,6,7,8,12,13},
        {1,3,5,6,7,8,12,13},
        {1,3,5,6,7,8,12,13},
        {1,3,5,6,7,8,12,13},
        {1,3,5,6,7,8,12,13},
        {1,2,3,6,7,8,12,13}
    };
    l=rlt[n-1].size();
    cout<<l<<"\n";
    for(int i=0;i<l;i++)
        cout<<(char)(rlt[n-1][i]+64)<<' ';
    return 0;
}