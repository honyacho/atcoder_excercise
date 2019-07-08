import scala.collection.mutable.Map
import scala.io.StdIn

object Main {
  val N = StdIn.readLine.toInt
  val Nd = N.toDouble
  val DP = Array.fill(N+2,N+2,N+2)(-1.0)

  def solve(i: Int, j: Int, k: Int): Double = {
    if (DP(i)(j)(k) >= 0.0) return DP(i)(j)(k)
    if (i+j+k == 0) return 0.0
    var res = 0.0
    if (i > 0) res = res + solve(i-1,j,k)*i
    if (j > 0) res = res + solve(i+1,j-1,k)*j
    if (k > 0) res = res + solve(i,j+1,k-1)*k
    res = res+Nd
    res = res/(i+j+k).toDouble
    DP(i)(j)(k) = res
    return res
  }

  def main(args: Array[String]) = {
    val N_inv = 1.0 / N.toDouble
    val INIT = Map(1 -> 0,2 -> 0,3 -> 0)
    for (i <- StdIn.readLine.split(" ").map(_.toInt)) INIT(i) = INIT(i)+1
    println(solve(INIT(1), INIT(2), INIT(3)))
  }
}
