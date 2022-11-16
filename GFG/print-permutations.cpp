#include <bits/stdc++.h>

using namespace std;

void printPermutations(string &s, int l, int r) {
  if (l == r) {
    cout << s << endl;
    return;
  }

  while(l<=r){
      swap(s[l], s[r++]);
      printPermutations(s, l + 1, r);
      
  }
}

int main() {
  string s = "123";

  // printPermutations(s);
  return 0;
}