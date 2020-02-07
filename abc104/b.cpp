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
  string S;
  cin >> S;
  ll L = S.size();
  if (S[0] != 'A') {
    cout << "WA" << endl;
    return 0;
  }
  ll cntC = 0;
  RNG(i, 2, L-1) {
    if (S[i] == 'C') cntC += 1;
  }
  if (cntC != 1) {
    cout << "WA" << endl;
    return 0;
  }
  auto cntCap = 0;
  REP(i, L) {
    if (S[i] <= 'Z') cntCap += 1;
  }
  if (cntCap != 2) {
    cout << "WA" << endl;
    return 0;
  }
  cout << "AC" << endl;
  return 0;
}
