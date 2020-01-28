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
const ll DVSR = 1e9+7;
template <typename T> T modpow(T base, T exp, T modulus) {
  base %= modulus; T result = 1;
  while (exp > 0) {
    if (exp & 1) result = (result * base) % modulus;
    base = (base * base) % modulus;
    exp >>= 1;
  }
  return result;
}


ll modpow(ll x, ll n) {
  ll res = 1;

  while (n > 0) {
    if (n&1) res = res*x%DVSR;
    x = x*x%DVSR;
    n /= 2;
  }
  return res;
}

int main(int argc, char const *argv[])
{
  ll N; cin >> N;
  vector<ll> CS(N);
  REP(i, N) cin >> CS[i];
  sort(CS.begin(), CS.end(), greater<ll>());
  ll res = 0;
  RNG(i, 1, N+1) {
    res += CS[i-1]*(i+1);
    res %= DVSR;
  }
  cout << (modpow(4,N-1)*res % DVSR) << endl;
}
