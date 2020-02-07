#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(ll i=0; i<(ll)(n); i++)
#define RNG(i,from,to) for(ll i=(from); i<(ll)(to); i++)
#define gcd(i,j) __gcd((i), (j))
typedef long long ll;
typedef pair<int, int> pii;
template<typename S, typename T> string to_string(pair<S, T> p) { return "("+to_string(p.first)+","+to_string(p.second)+")"; }
template<typename T> string to_string(T p[2]) { return "["+to_string(p[0])+","+to_string(p[1])+"]"; }
template<typename T> void println(T e){ cout << to_string(e) << endl; }
template<typename T> void println(const vector<T>& v){ cout << "[";for(const auto& e : v){ cout << to_string(e) << ","; }cout << "]";cout << endl; }
template<typename T> void println(const vector<vector<T>>& vv){ for(const auto& v : vv){ println(v); } }
template<typename Iter> void println(Iter first, Iter last){ for(auto it=first; it != last; it++){ cout << *it << " "; }; cout << endl; }
const ll DVSR = 1e9+7;


int main(int argc, char const *argv[])
{
  ll N; cin >> N;
  if (N==0) {
    cout << 0 << endl;
    return 0;
  }
  vector<ll> res(32);
  ll sm = 0;
  REP(i, 32) res[i] = 0;
  RNG(i, 1, 33) {
    ll cur = 1LL << i;
    if ((sm - N)%cur) {
      res[i-1] = 1;
      sm += cur/2*((i-1)%2 ? -1 : 1);
    }
  }
  ll st = 31;
  while (!res[st]) st--;
  for (int i = st; i >= 0; i--) cout << res[i];
  cout << endl;
  return 0;
}
