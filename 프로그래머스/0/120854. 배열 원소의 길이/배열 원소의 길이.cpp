#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> strlist) {
    vector<int> r;
    for(int i=0;i<strlist.size();i++) {
        r.push_back(strlist[i].length());
    }
    return r;
}