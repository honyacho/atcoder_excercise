#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i=0; i<(int)(n); i++)
#define RNG(i,from,to) for(int i=(from); i<(int)(to); i++)
#define gcd(i,j) __gcd((i), (j))
typedef long long ll;
typedef pair<int, int> pii;
template<typename T> void show(T e){ cout << e << endl; }
template<typename T> void show(const vector<T>& v){ for(const auto& e : v){ cout << e << " "; } cout << endl; }
template<typename T> void show(const vector<vector<T>>& vv){ for(const auto& v : vv){ show(v); } }
template<class Iter> void show(Iter first, Iter last){ for(auto it=first; it != last; it++){ cout << *it << " "; }; cout << endl; }
const ll DVSR = 10e9+7;


int main(int argc, char const *argv[])
{
  ll N, K; cin >> N >> K;
  ll halfK = K / 2, cnt1 = 0, cnt2 = 0;

  if (K%2 == 0) {
    RNG(i,1,N+1) {
      cnt1 += (i%K == 0);
      cnt2 += (i%K == halfK);
    }
  } else {
    RNG(i,1,N+1) if (i%K == 0) cnt1++;
  }
  cout << cnt1*cnt1*cnt1 + cnt2*cnt2*cnt2 << endl;
  return 0;
}
