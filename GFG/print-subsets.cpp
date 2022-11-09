#include <bits/stdc++.h>

using namespace std;

void printSubsets(string s, string curr = "", int idx = 0) {
  if (idx == s.length()) {
    cout << curr << endl;
    return;
  }

  // do not include this choice
  printSubsets(s, curr, idx + 1);

  // include this choice
  printSubsets(s, curr + s[idx], idx + 1);
}

int main() {
  string s = "shreyans";
  printSubsets(s);
  return 0;
}