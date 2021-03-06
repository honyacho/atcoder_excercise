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

typedef struct tani {
  ll mai;
  ll time;
};

typedef struct dst {
  ll mai;
  ll time;
};

typedef pair<ll, pll> pos;

int main(int argc, char const *argv[])
{
  ll N,M,S; cin >> N >> M >> S;
  ll MA = 0;
  priority_queue<pos, vector<pos>, greater<pos>> PQ;

  vector<vector<dst>> MP;
  MP.assign(N+1, vector<dst>(N+1));
  vector<tani> CST(N+1);
  REP(i, M) {
    ll u, v, a, b;
    MA = max(a, MA);
    MP[u][v] = dst{ a, b };
    MP[v][u] = dst{ a, b };
  }

  REP(i, N) {
    tani cst;
    cin >> cst.mai >> cst.time;
    CST[i+1] = cst;
  }
  vector<vecll> DP;
  DP.assign(N+1, vecll(MA*(N-1), 1e15));
  DP[1][0] = 0;

  PQ.push(pos(0, pll(1,  0)));
  // 最大枚数
  ll MXC = MA*(N-1);
  while (PQ.size()) {
    auto v = PQ.top();
    PQ.pop();
    ll cur = v.second.first;
    auto ex_cost = CST[cur];
    // REP(e)
    ll cnt = ex_cost.mai;
    ll cost = ex_cost.time;
    while (1) {
      if (DP[cur][cnt] > cost) {
        DP[cur][cnt] = cost;
        PQ.push(pos(cost, pll(cur, cnt)));
      }
      if (cnt == MXC) break;
      cnt = min(cnt+ex_cost.mai, MXC);
      cost += ex_cost.time;
    }

  }

  return 0;
}
