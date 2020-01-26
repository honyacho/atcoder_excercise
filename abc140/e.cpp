#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i=0; i<(int)(n); i++)
#define RNG(i,from,to) for(int i=(from); i<(int)(to); i++)
typedef long long ll;
typedef pair<int, int> pii;
template<typename T> void show(T e){ cout << e << endl; }
template<typename T> void show(const vector<T>& v){ for(const auto& e : v){ cout << e << " "; } cout << endl; }
template<typename T> void show(const vector<vector<T>>& vv){ for(const auto& v : vv){ show(v); } }
template<class Iter> void show(Iter first, Iter last){ for(auto it=first; it != last; it++){ cout << *it << " "; }; cout << endl; }

int main(int argc, char const *argv[])
{
  ll N;
  cin >> N;
  vector<ll> arr(N+1);
  unordered_map<ll, int> pos;
  RNG(i, 1, N+1) {
    cin >> arr[i];
    pos[arr[i]] = i;
  }
  set<ll> st{0, N+1};
  ll res = 0;
  for(ll snd = N; snd >= 1; snd--) {
    ll idx = pos[snd];

    auto it = st.lower_bound(idx);
    if (*it != N+1) {
      res += snd * (*next(it) - *it) * (idx-*prev(it));
    }
    if (*prev(it) != 0) {
      res += snd * (*prev(it)-*prev(prev(it))) * (*it-idx);
    }
    st.insert(idx);
  }
  cout << res << endl;
  // show(arr);
  return 0;
}
