#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i=0; i<(int)(n); i++)
#define RNG(i,from,to) for(int i=(from); i<(int)(to); i++)
#define gcd(i,j) __gcd((i), (j))
typedef long long ll;
typedef pair<int, int> pii;
template<typename S, typename T> string to_string(pair<S, T> p) { return "("+to_string(p.first)+","+to_string(p.second)+")"; }
template<typename T> string to_string(T p[2]) { return "["+to_string(p[0])+","+to_string(p[1])+"]"; }
template<typename T> void strprint(T e){ cout << to_string(e) << endl; }
template<typename T> void strprint(const vector<T>& v){ cout << "[";for(const auto& e : v){ cout << to_string(e) << ","; }cout << "]";cout << endl; }
template<typename T> void strprint(const vector<vector<T>>& vv){ for(const auto& v : vv){ strprint(v); } }
template<typename Iter> void strprint(Iter first, Iter last){ for(auto it=first; it != last; it++){ cout << *it << " "; }; cout << endl; }
const ll DVSR = 1e9+7;


int main(int argc, char const *argv[])
{
  ll N, K; cin >> N >> K;
  vector<ll> XS(N);
  REP(i, N) cin >> XS[i];
  ll res = 1e15;
  if (N == 1) {
    cout << abs(XS[0]) << endl;
    return 0;
  }
  REP(i, N-K+1) {
    auto width = XS[i+K-1] - XS[i];
    if (XS[i] >= 0) {
      width += abs(XS[i]);
    } else if (XS[i+K-1] <= 0) {
      width += abs(XS[i+K-1]);
    } else {
      width += min(abs(XS[i+K-1]), abs(XS[i]));
    }
    res = min(res, width);
  }
  cout << res << endl;
  return 0;
}
