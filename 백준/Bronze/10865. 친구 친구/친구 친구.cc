#include <iostream>
#include <map>
using namespace std;
int main(void) {
    int n,m,a,b;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin>>n>>m;
    map<int,int> dic;
    for(int i=1;i<n+1;i++)
        dic[i]=0;
    for(int i=0;i<m;i++) {
        cin>>a>>b;
        dic[a]+=1;
        dic[b]+=1;
    }
    for(int i=1;i<n+1;i++)
        cout<<dic[i]<<"\n";
    return 0;
}