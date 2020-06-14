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
  int N; cin >> N;
  vector<int> AS(N);
  REP(i, N) cin >> AS[i];
  sort(AS.begin(), AS.end());
  set<int> st;

  int res = 0;
  REP(i, N) {
    if ((i < N) && AS[i+1] == AS[i]) {
      st.insert(AS[i]);
      continue;
    }
    auto ok = true;
    RNG(k, 1, (int)(sqrt((double)AS[i])+1)) if (AS[i]%k == 0 && ((st.find(k) != st.end()) || st.find(AS[i]/k) != st.end())) {
      ok = false;
      break;
    }

    res += ok;
    st.insert(AS[i]);
  }
  cout << res << endl;
  return 0;
}
