#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i=0; i<(int)(n); i++)
#define RNG(i,from,to) for(int i=(from); i<(int)(to); i++)
#define gcd(i,j) __gcd((i), (j))
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<ll> vecll;
template<typename S, typename T> string to_string(pair<S, T> p) { return "("+to_string(p.first)+","+to_string(p.second)+")"; }
template<typename T> string to_string(T p[2]) { return "["+to_string(p[0])+","+to_string(p[1])+"]"; }
template<typename T> void println(T e){ cout << to_string(e) << endl; }
template<typename T> void println(const vector<T>& v){ cout << "[";for(const auto& e : v){ cout << to_string(e) << ","; }cout << "]";cout << endl; }
template<typename T> void println(const vector<vector<T>>& vv){ for(const auto& v : vv){ println(v); } }
template<typename Iter> void println(Iter first, Iter last){ for(auto it=first; it != last; it++){ cout << *it << " "; }; cout << endl; }
const ll DVSR = 1e9+7;


int main(int argc, char const *argv[])
{
  ll N, res = 10e12; cin >> N;
  vecll AS(N);
  vecll ACC(N);
  REP(i, N) {
    cin >> AS[i];
    AS[i] -= (i+1);
  }
  sort(AS.begin(), AS.end());
  int idx = N/2;
  ll sm1 = 0;
  REP(i, N) {
    sm1 += abs(AS[i]-AS[idx]);
  }
  if (idx > 0) {
    ll sm2 = 0;
    REP(i, N) {
      sm2 += abs(AS[i]-AS[idx-1]);
    }
    cout << min(sm1, sm2) << endl;
  } else {
    cout << sm1 << endl;
  }
  return 0;
}
// 8+6+4+2+2
