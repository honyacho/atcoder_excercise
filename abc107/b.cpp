#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i=0; i<(int)(n); i++)
#define RNG(i,from,to) for(int i=(from); i<(int)(to); i++)
#define gcd(i,j) __gcd((i), (j))
typedef long long ll;
typedef pair<int, int> pii;
template<typename S, typename T> string to_string(pair<S, T> p) { return "("+to_string(p.first)+","+to_string(p.second)+")"; }
template<typename T> string to_string(T p[2]) { return "["+to_string(p[0])+","+to_string(p[1])+"]"; }
template<typename T> void strprint(T e){ cout << to_string(e) << endl; }
template<typename T> void strprint(const vector<T>& v){ cout << "[";for(const auto& e : v){ cout << to_string(e) << ","; }cout << "]";cout << endl; }
template<typename T> void strprint(const vector<vector<T>>& vv){ for(const auto& v : vv){ strprint(v); } }
template<typename Iter> void strprint(Iter first, Iter last){ for(auto it=first; it != last; it++){ cout << *it << " "; }; cout << endl; }
const ll DVSR = 1e9+7;


int main(int argc, char const *argv[])
{
  ll H, W; cin >> H >> W;
  string MP[H];
  REP(i, H) {
    cin >> MP[i];
  }
  ll compH = 0, compW = 0;
  REP(i, H) {
    bool isEmpty = true;
    REP(j, W) {
      isEmpty = isEmpty && MP[i][j] == '.';
    }
    if (!isEmpty) {
      MP[compH] = MP[i];
      compH++;
    }
  }
  REP(j, W) {
    bool isEmpty = true;
    REP(i, compH) {
      isEmpty = isEmpty && MP[i][j] == '.';
    }
    if (!isEmpty) {
      REP(i, compH) {
        MP[i][compW] = MP[i][j];
      }
      compW++;
    }
  }
  REP(i,compH) {
    cout << MP[i].substr(0, compW) << endl;
  }
  return 0;
}
