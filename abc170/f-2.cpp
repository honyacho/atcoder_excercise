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


typedef tuple<ll, ll, ll> tll;
ll H, W, K;
ll S_i, S_j, G_i, G_j;
vector<string> MP;

ll dis[] = {1, 0, -1, 0};
ll djs[] = {0, 1, 0, -1};
vector<vector<ll>> RES;

int main(int argc, char const *argv[])
{
  cin >> H >> W >> K;
  cin >> S_i >> S_j >> G_i >> G_j;
  S_i--; S_j--; G_i--;G_j--;
  auto comp = [](tll a, tll b) { return get<0>(a) > get<0>(b); };
  priority_queue<tll, vector<tll>, decltype(comp)> PQ(comp);

  MP.resize(H);
  REP(i, H) cin >> MP[i];
  RES.assign(H, vecll(W));
  REP(i, H) REP(j, W) RES[i][j] = 1e10;
  RES[S_i][S_j] = 0;
  PQ.push(tll(0, S_i, S_j));

  while (PQ.size()) {
    //cout << PQ.size() << endl;
    auto tup = PQ.top(); PQ.pop();
    ll score = get<0>(tup);
    ll curr_i = get<1>(tup);
    ll curr_j = get<2>(tup);
    if (score > RES[curr_i][curr_j]) continue;
    auto cur = pll(curr_i, curr_j);
    REP(l, 4) {
      RNG(k, 1, K+1) {
        ll n_i = curr_i + k*dis[l];
        ll n_j = curr_j + k*djs[l];
        ll n_s = score+1;
        if (n_i < 0 || n_j < 0 || n_i >= H || n_j >= W) break;
        if (MP[n_i][n_j] == '@') break;
        if (RES[n_i][n_j] != (ll)1e10) continue;
        RES[n_i][n_j] = n_s;
        PQ.push(tll(n_s, n_i, n_j));
      }
    }
  }
  if (RES[G_i][G_j] == (ll)1e10) {
    cout << -1 << endl;
  } else {
    cout << RES[G_i][G_j] << endl;
  }
  return 0;
}
