#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    string name;
    int n;
    cin>>n;
    vector<string> names;
    for(int i=0;i<n;i++) {
        cin >> name;
        names.push_back(name);
        cin >> name;
        names.push_back(name);
    }
    for(int i=0;i<n;i++) {
        cout<<"Case "<<i+1<<": "<<names[2*i+1]<<", "<<names[2*i]<<"\n";
    }
    return 0;
}