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
  ll N, K; cin >> N >> K;
  vecll LI(N);
  REP(i, N) cin >> LI[i];
  sort(LI.begin(), LI.end());
  ll hi = 1000000000000000000;
  ll lo = -1000000000000000000;
  ll value_mid = 0;
  while (hi != lo) {
    ll cnt = 0;
    value_mid = lo + (hi - lo)/2;
    REP(i, N-1) {
      ll llo = 0, hhi = N-1-i, mmid = 0;
      while (hhi != llo) {
        mmid = (hhi + llo)/2;
        if (LI[i]*(LI[i] >= 0 ? LI[i+1+mmid] : LI[N-1-mmid]) < value_mid) llo = mmid + 1;
        else hhi = mmid;
      }
      cnt += llo;
    }
    if (cnt < K) lo = value_mid + 1;
    else hi = value_mid;
  }
  cout << lo-1 << endl;
  return 0;
}
