#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i=0; i<(int)(n); i++)
#define RNG(i,from,to) for(int i=(from); i<(int)(to); i++)
#define gcd(i,j) __gcd((i), (j))
typedef long long ll;
typedef pair<int, int> pii;
template<typename S, typename T> string to_string(pair<S, T> p) { return "("+to_string(p.first)+","+to_string(p.second)+")"; }
template<typename T> string to_string(T p[2]) { return "["+to_string(p[0])+","+to_string(p[1])+"]"; }
template<typename T> void println(T e){ cout << to_string(e) << endl; }
template<typename T> void println(const vector<T>& v){ cout << "[";for(const auto& e : v){ cout << to_string(e) << ","; }cout << "]";cout << endl; }
template<typename T> void println(const vector<vector<T>>& vv){ for(const auto& v : vv){ println(v); } }
template<typename Iter> void println(Iter first, Iter last){ for(auto it=first; it != last; it++){ cout << *it << " "; }; cout << endl; }
void printbin(ll v) { REP(i, 64) { cout << ((v >> (63-i)) & 1L); } cout << endl; }
const ll DVSR = 1e9+7;


bool rec(ll v, ll par, ll goal, ll &path, unordered_map<ll, vector<pair<ll,ll>>> &graph) {
  if (v == goal) {
    return true;
  }
  for (auto edge : graph[v]) {
    if (edge.first == par) continue;
    if (rec(edge.first, v, goal, path, graph)) {
      path |= (1LL << edge.second);
      return true;
    }
  }
  return false;
}

int main(int argc, char const *argv[])
{
  unordered_map<ll, vector<pair<ll,ll>>> mp;
  ll N, M;
  cin >> N;
  REP(i, N-1) {
    ll a, b;
    cin >> a >> b;
    a--; b--;
    auto itr = mp.find(a);
    if (itr == mp.end()) mp[a] = vector<pair<ll,ll>>();
    itr = mp.find(b);
    if (itr == mp.end()) mp[b] = vector<pair<ll,ll>>();

    mp[a].push_back(pair<ll, ll>(b, i));
    mp[b].push_back(pair<ll, ll>(a, i));
  }

  cin >> M;
  vector<ll> paths(M, 0);
  REP(i, M) {
    ll u, v;
    cin >> u >> v;
    u--; v--;
    rec(u, -1, v, paths[i], mp);
  }
  ll res = 0;
  for (ll bit = 0; bit < (1<<M); ++bit) {
    ll val = 0;
    REP(i, M) if (bit & (1LL<<i)) val |= paths[i];
    ll rest = N-1 - __builtin_popcountl(val);
    if (__builtin_popcountl(bit) % 2 == 0) res += (1LL<<rest);
    else res -= (1LL<<rest);
  }
  cout << res << endl;
  return 0;
}
