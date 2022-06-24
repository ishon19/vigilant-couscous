#include <bits/stdc++.h>

using namespace std;

int n = 3;
vector<int> subset;

void search(int k)
{
    if (k == n + 1)
    {
        // process subset
        for (int i = 1; i <= n; i++)
        {
            if (subset[i])
                cout << i << " ";
        }
    }
    else
    {
        // include k in the subset
        subset.push_back(k);
        search(k + 1);
        subset.pop_back();
        // don’t include k in the subset
        search(k + 1);
    }
}

int main()
{
    search(1);
    return 0;
}