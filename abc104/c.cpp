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
const ll DVSR = 1e9+7;
const ll LG = 1e15;

const ll UPB = 230001;
int main(int argc, char const *argv[])
{
  ll D, G; cin >> D >> G;
  G /= 100;
  vector<vector<ll>> DP(D, vector<ll>(UPB));
  vector<pair<ll,ll>> INL(D);
  REP(i, D) {
    REP(j, UPB) {
      DP[i][j] = LG;
    }
    DP[i][0] = 0;
    cin >> INL[i].first >> INL[i].second;
    INL[i].second /= 100;
  }
  // println(G);
  // println(INL);
  REP(i, D) {
    ll score = i+1;
    if (i == 0) {
      RNG(k, 1, INL[i].first) {
        DP[i][score*k] = k;
      }
      DP[i][score*INL[i].first + INL[i].second] = INL[i].first;
    } else {
      RNG(k, 1, INL[i].first) {
        RNG(j, 0, UPB-20000) {
          DP[i][j + score*k] = min(DP[i-1][j]+k, DP[i-1][j + score*k]);
        }
      }
      RNG(j, 0, UPB-20000) {
        DP[i][j + score*INL[i].first + INL[i].second] = min(DP[i-1][j]+INL[i].first, DP[i-1][j + score*INL[i].first + INL[i].second]);
      }
    }
  }
  ll res = LG;
  RNG(i, G, UPB) {
    res = min(res, DP[D-1][i]);
  }
  println(res);
  return 0;
}
