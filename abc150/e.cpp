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
template <typename T> T modpow(T base, T exp, T modulus) {
  base %= modulus; T result = 1;
  while (exp > 0) {
    if (exp & 1) result = (result * base) % modulus;
    base = (base * base) % modulus;
    exp >>= 1;
  }
  return result;
}

int main(int argc, char const *argv[])
{
  ll N; cin >> N;
  vector<ll> CS(N);
  REP(i, N) cin >> CS[i];
  vector<ll> facts(N+1), CUM(N+1);
  facts[0] = 1;
  CUM[0] = 0;
  RNG(i,1,N+1) facts[i] = facts[i-1]*i % DVSR;
  sort(CS.begin(), CS.end());
  REP(i, N+1) {}
  return 0;
}
