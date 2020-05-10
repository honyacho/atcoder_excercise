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

ll ARR[200010];
ll LST[200010];

int main(int argc, char const *argv[])
{
  ll N, K; cin >> N >> K;
  RNG(i, 1, N+1) cin >> ARR[i];
  REP(i, 200010) LST[i] = -1;

  ll next = 1, cnt = 0;
  while (LST[next] == -1) {
    if (cnt == K) {
      cout << next << endl;
      return 0;
    }
    LST[next] = cnt;
    cnt++;
    next = ARR[next];
  }

  K -= cnt;
  K %= (cnt-LST[next]);
  // cout << "loop made: " << cnt << endl;
  // cout << "LOOP toutatu made: " << LST[next] << endl;
  // cout << "LOOP len: " << cnt-LST[next] << endl;
  // cout << "K: " << K << endl;

  if (K == 0) {
    cout << next << endl;
  } else {
    cnt = 1; next = ARR[next];
    while (cnt < K) {
      cnt++;
      next = ARR[next];
    }
    cout << next << endl;
  }
  return 0;
}
