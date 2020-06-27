#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(ll i=0; i<(ll)(n); i++)
#define RNG(i,from,to) for(ll i=(from); i<(ll)(to); i++)
#define gcd(i,j) __gcd((i), (j))
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll,ll> pll;
typedef vector<ll> vecll;
template<typename S, typename T> string to_string(pair<S, T> p) { return "("+to_string(p.first)+
+to_string(p.second)+")"; }
template<typename T> void println(T e){ cout << to_string(e) << endl; }
template<typename T> void println(const vector<T>& v){ cout << "[";for(const auto& e : v){ cout << to_string(e) << ","; } cout << "]"; cout << endl; }
template<typename T> void println(const vector<vector<T>>& vv){ for(const auto& v : vv){ println(v); } }
template<typename Iter> void println(Iter first, Iter last){ for(auto it=first; it != last; it++){ cout << *it << " "; }; cout << endl; }
template<typename T> T mod_pow(T x, T n, const T &p) { T ret = 1; while(n > 0) { if(n & 1) (ret *= x) %= p; (x *= x) %= p; n >>= 1; } return ret; }
template<typename T> T mod_inv(T x, const T &p) { return mod_pow(x, p-2, p); }
const ll DVSR = 1e9+7;
typedef tuple<ll, ll, ll, ll> sc_t;

ll H, W, K;
ll Si, Sj, Gi, Gj;
vector<string> MP;
vector<vector<ll>> RES;
vector<vector<vector<ll>>> RES2;

priority_queue<sc_t, vector<sc_t>, greater<>> PQ;
ll dis[] = {1, 0, -1, 0};
ll djs[] = {0, 1, 0, -1};

void solve() {
  while (PQ.size()) {
    sc_t sc = PQ.top(); PQ.pop();
    ll score = get<0>(sc);
    ll dir = get<1>(sc);
    ll i = get<2>(sc);
    ll j = get<3>(sc);

    RES[i][j] = min(RES[i][j], score);
    if (dir >= 0) RES2[i][j][dir] = min(RES2[i][j][dir], score);
    REP(nd, 4) {
      ll ni = i + dis[nd];
      ll nj = j + djs[nd];
      if (ni >= 0 && ni < H && nj >= 0 && nj < W && MP[ni][nj] == '.') {
        auto next_sc = score;
        if (dir != nd && dir != -1 && (next_sc % K)) {
          next_sc -= (next_sc % K);
          next_sc += K;
        }
        next_sc += 1;

        if (next_sc < RES[ni][nj]) {
          RES[ni][nj] = min(RES[ni][nj], next_sc);
          RES2[ni][nj][nd] = min(RES2[ni][nj][nd], next_sc);
          PQ.push(sc_t(next_sc, nd, ni, nj));
        } else if (next_sc < RES2[ni][nj][nd]) {
          RES2[ni][nj][nd] = min(RES2[ni][nj][nd], next_sc);
          PQ.push(sc_t(next_sc, nd, ni, nj));
        }
      }
    }
  }
}

int main(int argc, char const *argv[])
{
  cin >> H >> W >> K;
  cin >> Si >> Sj >> Gi >> Gj;
  Si--; Sj--; Gi--; Gj--;

  ll INF = 1000000000LL*1000000000LL;
  MP.resize(H);
  RES.assign(H, vector<ll>(W, INF));
  RES2.assign(H, vector<vector<ll>>(W, vector<ll>{ INF, INF, INF, INF }));
  REP(i, H) cin >> MP[i];
  PQ.push(sc_t(0, -1, Si, Sj));
  RES[Si][Sj] = 0;
  solve();  if (RES[Gi][Gj] == INF) {
    cout << -1 << endl;
  } else {
    cout << RES[Gi][Gj]/K + (RES[Gi][Gj]%K > 0) << endl;
  }

  return 0;
}
