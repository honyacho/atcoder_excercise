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

class UnionFind
{
  public:
    vecll nodes;
    UnionFind(int l);
    void unite(ll i, ll j);
    ll find(ll x);
    bool is_same(ll i, ll j);
};

UnionFind::UnionFind(int l)
{
  nodes = vector<ll>(l+1);
  REP(i, l+1) nodes[i] = i;
}

ll UnionFind::find(ll x)
{
  if (nodes[x] == x) return x;

  ll parent = find(nodes[x]);
  nodes[x] = parent;
  return parent;
}

void UnionFind::unite(ll i, ll j)
{
  ll a = find(i);
  ll b = find(j);
  if (a == b) {
    return;
  } else {
    nodes[a] = nodes[b];
  }
}

bool UnionFind::is_same(ll i, ll j)
{
  return find(i) == find(j);
}

int main(int argc, char const *argv[])
{
  return 0;
}