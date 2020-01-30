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
  ll N; cin >> N;
  vector<ll[2]> coord(N);
  REP(i, N) {
    cin >> coord[i][0] >> coord[i][1];
  }
  double res = 1e15;
  if (N==2) {
    strprint(0.5*sqrt((coord[0][0]-coord[1][0])*(coord[0][0]-coord[1][0]) + (coord[0][1]-coord[1][1])*(coord[0][1]-coord[1][1])));
    return 0;
  }
  RNG(i, 0, N-2) {
    RNG(j, i+1, N-1) {
      RNG(k, j+1, N) {
        double M11 = coord[i][0] - coord[j][0], M12 = coord[i][1] - coord[j][1];
        double M21 = coord[j][0] - coord[k][0], M22 = coord[j][1] - coord[k][1];
        double v1 = (coord[i][0]*coord[i][0]+coord[i][1]*coord[i][1]) - (coord[j][0]*coord[j][0]+coord[j][1]*coord[j][1]);
        double v2 = (coord[j][0]*coord[j][0]+coord[j][1]*coord[j][1]) - (coord[k][0]*coord[k][0]+coord[k][1]*coord[k][1]);
        double lmd = 0.5/(M11*M22-M21*M12);
        double a = lmd*(M22*v1 - M12*v2);
        double b = lmd*(-M21*v1 + M11*v2);
        double r = sqrt((coord[i][0]-a)*(coord[i][0]-a) + (coord[i][1]-b)*(coord[i][1]-b));
        // strprint(res);
        bool ok = true;
        REP(l, N) {
          double r2 = sqrt((coord[l][0]-a)*(coord[l][0]-a) + (coord[l][1]-b)*(coord[l][1]-b));
          if (r2 > r + 0.0000001) {
            ok = false;
          }
        }
        // if (ok) strprint(r);
        if (ok && r < 1e15) res = min(r, res);
      }
    }
  }
  RNG(i, 0, N-1) {
    RNG(j, i+1, N) {
      double med_x = (coord[j][0]+coord[i][0])*0.5, med_y = (coord[j][1]+coord[i][1])*0.5;
      double r = 0.5*sqrt((coord[j][0]-coord[i][0])*(coord[j][0]-coord[i][0]) + (coord[j][1]-coord[i][1])*(coord[j][1]-coord[i][1]));
      bool ok = true;
      REP(k, N) {
        ok = ok && sqrt((coord[k][0]-med_x)*(coord[k][0]-med_x) + (coord[k][1]-med_y)*(coord[k][1]-med_y)) < r+0.000001;
      }
      if (ok) res = min(res, r);
    }
  }
  std::cout << std::setprecision(15) << res << endl;
  return 0;
}
