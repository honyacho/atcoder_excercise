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
const ll DVSR = 1e9+7;


int main(int argc, char const *argv[])
{
  ll N, K; cin >> N >> K;
  vecll LI(N);
  REP(i, N) cin >> LI[i];
  sort(LI.begin(), LI.end());
  ll mm = *LI.begin();
  ll MM = *(LI.end() - 1);
  ll hi = max(MM*MM, mm*mm)+1;
  ll lo = min(min(mm*mm, MM*mm), MM*MM);
  ll value_mid = 0;
  int zeroIdx = lower_bound(LI.begin(), LI.end(), 0LL) - LI.begin();
  while (hi != lo) {
    value_mid = lo + (hi - lo)/2;    
    ll cnt = 0, lft = 0, rgt = zeroIdx;
    // --
    while (lft < rgt) {
      if (LI[lft]*LI[rgt-1] < value_mid) {
        cnt += rgt - lft - 1;
        rgt -= 1;
      } else {
        lft += 1;
      }
    }

    // -+
    lft = 0;
    rgt = zeroIdx+1;
    while (rgt <= N && LI[lft] < 0 && LI[rgt-1] >= 0) {
      if (LI[lft]*LI[rgt-1] < value_mid) {
        cnt += N - rgt + 1;
        lft += 1;
      } else {
        rgt += 1;
      }
    }

    // ++
    lft = zeroIdx;
    rgt = N;
    while (lft < rgt) {
      if (LI[lft]*LI[rgt-1] < value_mid) {
        cnt += rgt - lft - 1;
        lft += 1;
      } else {
        rgt -= 1;
      }
    }
    if (cnt < K) lo = value_mid + 1;
    else hi = value_mid;
  }
  std::cout << (lo-1) << endl;
  return 0;
}
