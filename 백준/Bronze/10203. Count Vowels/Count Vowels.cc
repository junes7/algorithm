#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    int n, cnt;
    string st;
    vector<char> vowel = {'a', 'e', 'i', 'o', 'u'};
    cin >> n;
    for (int i = 0; i < n; i++) {
        cnt = 0;
        cin >> st;
        for (int j = 0; j < st.size(); j++) {
            if (find(vowel.begin(), vowel.end(), st[j]) != vowel.end())
                cnt += 1;
        }
        cout << "The number of vowels in " << st << " is " << cnt << ".\n";
    }
    return 0;
}