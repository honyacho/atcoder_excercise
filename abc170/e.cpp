#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i=0; i<(int)(n); i++)
#define RNG(i,from,to) for(int i=(from); i<(int)(to); i++)
#define gcd(i,j) __gcd((i), (j))
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

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

// rate, you の順
set<pair<ll,ll>> score;
// you rate の順
map<pair<ll,ll>, ll> to_count;

pair<ll,ll> npr(ll i, ll j) {
  return pair<ll,ll>(i,j);
}

int main(int argc, char const *argv[])
{
  ll N, Q; cin >> N >> Q;
  vector<pair<ll,ll>> to_info(N+1);

  RNG(i, 1, N+1) {
    ll RATE, YOU;
    cin >> RATE >> YOU;
    auto pr = npr(YOU, RATE);
    to_info[i] = pr;
    if (to_count.find(pr) != to_count.end()) {
      to_count[pr] += 1;
    } else {
      to_count[pr] = 1;
    }
  }

  ll you = to_count.begin()->first.first;
  ll cur_max = to_count.begin()->first.second;
  for (const auto& kv: to_count) {
    if (kv.first.first == you) {
      cur_max = max(cur_max, kv.first.second);
    } else {
      score.insert(npr(cur_max, you));
      you = kv.first.first;
      cur_max = kv.first.second;
    }
  }

  REP(i, Q) {
    ll C, D; cin >> C >> D;
    auto pr = to_info[C];
    auto rev_pr = npr(pr.second, pr.first);
    // 最高値だった場合
    if (score.find(rev_pr) != score.end()) {
      score.erase(rev_pr);
      // 存在チェック
      if (to_count.lower_bound(npr(pr.first, 0)) != to_count.lower_bound(npr(pr.first+1, 0))) {

      }
    }
  }
  return 0;
}
