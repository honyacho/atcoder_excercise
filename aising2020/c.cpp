#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(ll i=0; i<(ll)(n); i++)
#define RNG(i,from,to) for(ll i=(from); i<(ll)(to); i++)
#define gcd(i,j) __gcd((i), (j))
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll,ll> pll;
typedef vector<ll> vecll;
template<typename S, typename T> string to_string(pair<S, T> p) { return "("+to_string(p.first)+","+to_string(p.second)+")"; }
template<typename T> void println(T e){ cout << to_string(e) << endl; }
template<typename T> void println(const vector<T>& v){ cout << "[";for(const auto& e : v){ cout << to_string(e) << ","; }cout << "]";cout << endl; }
template<typename T> void println(const vector<vector<T>>& vv){ for(const auto& v : vv){ println(v); } }
template<typename Iter> void println(Iter first, Iter last){ for(auto it=first; it != last; it++){ cout << *it << " "; }; cout << endl; }
template<typename T> T mod_pow(T x, T n, const T &p) { T ret = 1; while(n > 0) { if(n & 1) (ret *= x) %= p; (x *= x) %= p; n >>= 1; } return ret; }
template<typename T> T mod_inv(T x, const T &p) { return mod_pow(x, p-2, p); }
const ll DVSR = 1e9+7;

int main(int argc, char const *argv[])
{

  ll N; cin >> N;

  ll pat = 0;
  RNG(i, 1, N+1) {
    ll cnt = 0;
    ll current = i;
    RNG(x, 1, (ll)sqrt(i)+1) {
      ll tmp1 = current - x*x;
      if (tmp1 > 0) {
        RNG(y, 1, (ll)sqrt(tmp1)+1) {
          ll c = -tmp1 + y*y + x*y;
          if (-c <= 0) break;

          ll b = y+x;
          double d = sqrt(b*b - 4*c);
          ll z = (ll)((-(double)b + d)/2.0);
          cnt += (z > 0 && z*z + z*y + z*x + c == 0);
        }
      }
    }
    cout << cnt << endl;
  }
  return 0;
}
