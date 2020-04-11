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


int main(int argc, char const *argv[])
{
  ll N, K, C, cur = 0, br = 2000000000; cin >> N >> K >> C;
  string S; cin >> S;
  vecll work(K), work2(K);
  REP(i, N) if (cur < K) {
    if (br >= C && S[i] == 'o') {
      work[cur] = i;
      cur++;
      br = 0;
    } else br++;
  } else break;

  cur = 0;
  br = 2000000000;
  REP(i, N) {
    ll j = N-i-1;
    if (cur < K) {
      if (br >= C && S[j] == 'o') {
        work2[K-cur-1] = j;
        cur++;
        br = 0;
      } else br++;
    } else break;
  }
  REP(i, K) if (work[i] == work2[i]) cout << work[i]+1 << endl;
  return 0;
}
