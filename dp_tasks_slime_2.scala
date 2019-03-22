import scala.io.Source

object Main {
  def main(args: Array[String]) = {
    val lines = Source.stdin.getLines.toStream
    val input = lines.drop(1).head.split(' ').map(_.toLong)

    val memo = Array.fill(input.length + 1, input.length + 1, 2)(-1L)
    (1 to input.length).foreach { n =>
      memo(n-1)(n)(0) = input(n-1)
      memo(n-1)(n)(1) = 0
    }

    val res = dp(input, 0, input.length, memo)
    println(res(1))
  }

  def dp(input: IndexedSeq[Long], left: Int, right: Int, memo: Array[Array[Array[Long]]]): Array[Long] = {
    if (memo(left)(right)(0) != -1L) return memo(left)(right)

    var minCost = Long.MaxValue
    var minTotal = Long.MaxValue
    ((left + 1) to (right - 1)).foreach { split =>
      val leftRes = dp(input, left, split, memo)
      val rightRes = dp(input, split, right, memo)
      val cost = leftRes(0) + rightRes(0)
      val total = leftRes(1) + rightRes(1) + leftRes(0) + rightRes(0)
      if (total < minTotal) {
        minCost =  cost
        minTotal = total
      }
    }
    memo(left)(right)(0) = minCost
    memo(left)(right)(1) = minTotal
    memo(left)(right)
  }
}
