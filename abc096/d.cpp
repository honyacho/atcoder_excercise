#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i=0; i<(int)(n); i++)
#define RNG(i,from,to) for(int i=(from); i<(int)(to); i++)
#define gcd(i,j) __gcd((i), (j))
typedef int64_t ll;
typedef int32_t ii;
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
  int32_t N; cin >> N;
  map<int32_t, vector<ii>> mp;
  vector<ii> visited(N+1);
  visited.assign(N+1, 0);
  queue<pair<int32_t, int32_t>> q1;

  REP(i, N-1) {
    int32_t k, v;
    cin >> k >> v;
    if (mp.find(k) == mp.end()) mp[k] = vector<ii>();
    if (mp.find(v) == mp.end()) mp[v] = vector<ii>();
    mp[k].push_back(v);
    mp[v].push_back(k);
  }
  visited[1] = 1;
  visited[N] = 2;
  q1.push(pair<int32_t, int32_t>(1, 1));
  q1.push(pair<int32_t, int32_t>(N, 2));
  while (q1.size()) {
    while (q1.size() && q1.front().second == 1) {
      int v = q1.front().first;
      q1.pop();
      for (const auto& nx: mp[v])
      if (!visited[nx]) {
        q1.push(pair<ii,ii>(nx, 1));
        visited[nx] = 1;
      }
    }
    while (q1.size() && q1.front().second == 2) {
      int v = q1.front().first;
      q1.pop();
      for (const auto& nx: mp[v]) {
        if (!visited[nx]) {
          q1.push(pair<ii,ii>(nx, 2));
          visited[nx] = 2;
        }
      }
    }
  }
  // println(visited);
  ii feneck = 0, sunuke = 0;
  RNG(i, 1, N+1) {
    if (visited[i] == 1) feneck += 1;
    if (visited[i] == 2) sunuke += 1;
  }
  // cout << feneck << " " << sunuke << endl;
  if (feneck > sunuke) {
    cout << "Fennec" << endl;
  } else {
    cout << "Snuke" << endl;
  }

  return 0;
}
