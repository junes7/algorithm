#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    vector<int> price(3),plan(3),unit={100,50,20};
    int total=0;
    for(int i=0;i<3;i++)
        cin>>price[i];
    for(int i=0;i<3;i++)
        cin>>plan[i];
    for(int i=0;i<3;i++)
        total+=plan[i]/unit[i]*price[i];
    cout<<total;
    return 0;
}