#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i=0; i<(int)(n); i++)
#define RNG(i,from,to) for(int i=(from); i<(int)(to); i++)
#define gcd(i,j) __gcd((i), (j))
typedef long long ll;
typedef pair<int, int> pii;
template<typename T> void show(T e){ cout << e << endl; }
template<typename T> void show(const vector<T>& v){ for(const auto& e : v){ cout << e << " "; } cout << endl; }
template<typename T> void show(const vector<vector<T>>& vv){ for(const auto& v : vv){ show(v); } }
template<class Iter> void show(Iter first, Iter last){ for(auto it=first; it != last; it++){ cout << *it << " "; }; cout << endl; }
const ll DVSR = 10e9+7;


int main(int argc, char const *argv[])
{
  ll x1,y1,x2,y2; cin >> x1 >> y1 >> x2 >> y2;
  cout << (x2 - (y2 - y1)) << " " << (y2 + (x2 - x1)) << " "
    << (x1 - (y2 - y1)) << " " << (y1 + (x2 - x1)) << endl;
  return 0;
}
