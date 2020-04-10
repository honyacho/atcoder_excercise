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
template<typename T> T mod_pow(T x, T n, const T &p) { T ret = 1; while(n > 0) { if(n & 1) (ret *= x) %= p; (x *= x) %= p; n >>= 1; } return ret; }
template<typename T> T mod_inv(T x, const T &p) { return mod_pow(x, p-2, p); }
const ll DVSR = 1e9+7;

bool ok(ll N, ll K) {
  if (N == 1) return true;
  if (N % K == 1) {
    return true;
  } else if (N % K == 0) {
    return ok(N/K, K);
  } else {
    return false;
  }
}

int main(int argc, char const *argv[])
{
  ll N; cin >> N;
  ll NN = N-1;
  ll cnt = 2;
  if (N == 2) {
    cout << 1 << endl;
    return 0;
  }
  ll upper = sqrt(NN)+1;
  for (ll i = 2; i < upper; i++) {
    if (NN%i == 0) {
      // cout << i << " " << NN/i << endl;
      if (i*i != NN) {
        cnt += 2;
      } else cnt += 1;
    }
  }
  // cout << "ok" << endl;
  RNG(i, 2, sqrt(N)+1) {
    if (N%i != 1 && ok(N, i)) {
      // cout << i << endl;
      cnt++;
    }
  }
  cout << cnt << endl;
  return 0;
}
