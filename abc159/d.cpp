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

vecll AS(200001);
int main(int argc, char const *argv[])
{
  ll N; cin >> N;
  unordered_map<ll, ll> MP;
  REP(i, N) {
    cin >> AS[i];
    auto itr = MP.find(AS[i]);
    if (itr != MP.end()) itr->second += 1;
    else MP.insert(pair<ll, ll>(AS[i], 1LL));
  }
  ll SM = 0;
  for (const auto &pr : MP) SM += pr.second*(pr.second-1)/2;
  REP(i, N) {
    ll cnt = MP.find(AS[i])->second;
    ll res = SM - cnt*(cnt-1)/2 + (cnt-1)*(cnt-2)/2;
    cout << res << endl;
  }
  return 0;
}
