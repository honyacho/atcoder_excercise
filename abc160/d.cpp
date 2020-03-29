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
  int N, X, Y; cin >> N >> X >> Y;
  set<int> ST;
  RNG(K, 1, N) {
    int cnt = 0;
    RNG(i, 1, N+1) {
      int distX = abs(X-i),
          distY = abs(Y-i),
          rgt = i + K,
          lft2 = Y-(K-distX-1),
          rgt2 = Y+(K-distX-1),
          lft3 = X-(K-distY-1),
          rgt3 = X+(K-distY-1);

      if (rgt <= N && distX+abs(rgt-Y)+1 >= K && distY+abs(rgt-X)+1 >= K) ST.insert(rgt);
      if (rgt2 > i && rgt2 > 0 && rgt2 <= N && abs(rgt2-i) >= K && K > distX) ST.insert(rgt2);
      if (lft2 > i && lft2 > 0 && lft2 <= N && abs(lft2-i) >= K && K > distX) ST.insert(lft2);
      if (rgt3 > i && rgt3 > 0 && rgt3 <= N && abs(rgt3-i) >= K && K > distY) ST.insert(rgt3);
      if (lft3 > i && lft3 > 0 && lft3 <= N && abs(lft3-i) >= K && K > distY) ST.insert(lft3);
      // for (const auto& v: ST) cout << "i: " << i << " v: " << v << endl;
      cnt += ST.size();
      ST.clear();
    }
    cout << cnt << endl;
  }
  return 0;
}
