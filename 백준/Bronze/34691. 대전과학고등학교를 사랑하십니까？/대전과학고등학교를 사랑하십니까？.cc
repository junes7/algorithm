#include <iostream>
using namespace std;
int main(void) {
    string word;
    while(cin>>word) {
        if(word=="end") break;
        if(word=="animal") {
            cout<<"Panthera tigris\n";
        } else if(word=="tree") {
            cout<<"Pinus densiflora\n";
        } else if(word=="flower") {
            cout<<"Forsythia koreana\n";
        }
    }
    return 0;
}