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

// mod. m での a の逆元 a^{-1} を計算する
ll modinv(ll a, ll m) {
  ll b = m, u = 1, v = 0;
  while (b) {
    ll t = a / b;
    a -= t * b; swap(a, b);
    u -= t * v; swap(u, v);
  }
  u %= m;
  if (u < 0) u += m;
  return u;
}
ll fact[2000020];

ll comb(ll n, ll r) {
  ll res = 1;
  res *= fact[n];
  res %= DVSR;
  res *= modinv(fact[n-r], DVSR);
  res %= DVSR;
  res *= modinv(fact[r], DVSR);
  res %= DVSR;
  return res;
}

ll g(ll r, ll c) {
  return comb(r+c+2, r+1)-1;
}

int main(int argc, char const *argv[])
{
  ll r1, c1, r2, c2; cin >> r1 >> c1 >> r2 >> c2;
  r1--;
  c1--;
  fact[0] = 1;
  RNG(i, 1, 2000020) {
    fact[i] = (fact[i-1]*i) % DVSR;
  }


  ll res = g(r2,c2) - g(r1, c2) - g(r2, c1) + g(r1, c1);
  res %= DVSR;
  res += DVSR;
  res %= DVSR;
  cout << res << endl;

  return 0;
}
