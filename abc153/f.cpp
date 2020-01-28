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

class Bit {
  public:
  Bit(int size);
  ll sum(int i);
  void add(int i, ll x);
  private:
  ll size;
  vector<ll> tree;
};

Bit::Bit(int n) {
  size = n;
  tree = vector<ll>(n+10);
};

ll Bit::sum(int i) {
  i = i+1;
  ll s = 0;
  while (i > 0) {
    s += tree[i];
    i -= i & -i;
  }
  return s;
};

void Bit::add(int i, ll x) {
  i = i+1;
  while (i <= size) {
    tree[i] += x;
    i += i & -i;
  }
};

class RBit {
  public:
  RBit(int n, Bit *bit);
  void add(ll x, int left, int right);
  ll sum(int i);
  ll get(int i);
  private:
  Bit *bit0;
  Bit *bit1;
};

RBit::RBit(int n, Bit *bit) {
  bit0 = bit;
  bit1 = new Bit(n);
};

void RBit::add(ll x, int left, int right) {
  bit0->add(left, -x*(left-1));
  bit1->add(left, x);
  bit0->add(right+1, x*right);
  bit1->add(right+1, -x);
};

ll RBit::sum(int i) {
  return bit1->sum(i)*i + bit0->sum(i);
};
ll RBit::get(int i) {
  return this->sum(i) - (i > 0 ? this->sum(i-1) : 0);
};

int main(int argc, char const *argv[])
{
  ll N, D, A; cin >> N >> D >> A;
  vector<pair<ll,ll>> LIN(N);
  vector<ll> POS(N);
  auto init = new Bit(N);

  REP(i, N) {
    ll a, b;
    cin >> a >> b;
    LIN[i] = pair<ll,ll>(a, b);
  }
  sort(LIN.begin(), LIN.end());
  REP(i, N) {
    POS[i] = LIN[i].first;
    init->add(i, LIN[i].second);
  }
  auto rbit = new RBit(N, init);

  ll res = 0;
  REP(i, N) {
    ll hp = rbit->get(i);
    // show(hp);
    if (hp > 0) {
      ll atc_cnt = hp / A + (hp%A > 0 ? 1 : 0);
      auto it = upper_bound(POS.begin(), POS.end(), POS[i]+2*D);
      int right = (it - POS.begin()) - 1;
      // show(right);
      rbit->add(-A*atc_cnt, i, right);
      res += atc_cnt;
    }
  }
  show(res);
  return 0;
}
