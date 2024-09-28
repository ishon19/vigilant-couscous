class Solution {
public:
    int largestVariance(string s) {
        int res = 0;
        unordered_set<char> unique(begin(s), end(s));

        for (char a: unique) {
            for (char b: unique) {
                int diff = 0;
                int has_b = 0;
                int first_b = 0;

                for (auto ch: s) {
                    diff += ch == a;
                    if (ch == b) {
                        has_b = true;
                        // we need to have atleast one b
                        if (first_b && diff>=0) {
                            first_b = false;
                        } else if(--diff < 0) {
                            first_b = true;
                            diff = -1;
                        }
                    }                 
                 res = max(res, has_b ? diff: 0);
                }
            }
        }

        return res;
    }
};