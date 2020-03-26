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
  ll H,W,K; cin >> H >> W >> K;
  vector<int> MP(1000);
  string line;
  vector<int> ACC(H);
  vector<int> CURR(H);

  REP(i, 1000) MP[i] = 0;
  REP(j, H) {
    cin >> line;
    REP(i, W) {
      if (line[i] == '1') {
        MP[j] |= (1 << i);
      }
    }
  }

  int res = H*W;
  REP(k, 1 << (H-1)) {
    int cnt_brr = 0;
    REP(i, H) {
      ACC[i] = 0;
      CURR[i] = 0;
    }
    REP(i, 10) cnt_brr += (k >> i) & 1;
    cout << "init cnt_brr: " << cnt_brr << endl;
    REP(j, W) {
      REP(i, H) CURR[i] = 0;
      int part = 0, i = 0, bound = 1;
      bool isBarrier = false;
      while (bound <= H) {
        while (!(k & (1 << (bound-1))) && bound < H) bound++;
        while (i < bound) {
          CURR[part] += 1 & (MP[i] >> j);
          i++;
        }
        isBarrier = isBarrier || CURR[part]+ACC[part] > K;
        part++;
        bound++;
      }
      REP(i, H) if (CURR[i] > K) {
        cnt_brr = H*W;
        break;
      }
      if (isBarrier) {
        REP(i, H) {
          cout << ACC[i] << " ";
          ACC[i] = CURR[i];
          CURR[i] = 0;
        }
        cout << endl;
        cnt_brr++;
        cout << "add brr: " << j << endl;
      } else {
        REP(i, H) ACC[i] += CURR[i];
      }
    }
    res = min(res, cnt_brr);
  }
  cout << res << endl;
  return 0;
}
