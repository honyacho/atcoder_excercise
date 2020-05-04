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

ll SCORE = 0;
int conds[100][4];

void calc(int idx, int minv, int N, int M, int Q, vector<ll> &arr)
{
  ll score = 0;
  if (idx < N)
    RNG(i, minv, M+1) {
      arr[idx] = i;
      calc(idx+1, arr[idx], N, M, Q, arr);
    }
  else
    REP(i, Q) if (arr[conds[i][1]-1] - arr[conds[i][0]-1] == conds[i][2]) {
      score += conds[i][3];
      SCORE = max(score, SCORE);
    }
}

int main(int argc, char const *argv[])
{
  ll N, M, Q; cin >> N >> M >> Q;
  REP(i, Q) cin >> conds[i][0] >> conds[i][1] >> conds[i][2] >> conds[i][3];
  vecll arr(11);
  REP(i, 11) arr[i] = 0;

  calc(0, 1, N, M, Q, arr);
  cout << SCORE << endl;
  return 0;
}
