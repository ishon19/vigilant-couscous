#include <bits/stdc++.h>

using namespace std;

vector<vector<string>> groupAnagrams(vector<string> &strs) {
  unordered_map<string, vector<string>> mp;
  for (string s : strs) {
    string t = s;
    sort(t.begin(), t.end());
    mp[t].push_back(s);
  }
  vector<vector<string>> res;
  for (auto p : mp) {
    res.push_back(p.second);
  }
  return res;
}

int main() {
  vector<string> vec = {"bat", "tab", "bad", "dab"};
  vector<vector<string>> ret = groupAnagrams(vec);
  for (auto i : ret) {
    for (string j : i) {
      cout << j << " ";
    }
    cout << endl;
  }
  return 0;
}