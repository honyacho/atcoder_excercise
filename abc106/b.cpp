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


int main(int argc, char const *argv[])
{
  ll N; cin >> N;
  vector<ll> res = {};
  ll resint = 0;
  RNG(i, 1, N+1) {
    if (i%2 == 0) continue;

    ll cnt = 0;
    RNG(j, 1, ((ll)sqrt(i)) + 1) {
      if (i % j == 0) {
        if (j*j == i) {
          cnt += 1;
        } else {
          cnt += 2;
        }
      }
    }
    if (cnt == 8) {
      resint++;
    }
  }
  println(resint);
  return 0;
}
