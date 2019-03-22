import scala.io.Source

object Main {
  def main(args: Array[String]) = {
    val lines = Source.stdin.getLines.toStream
    val input = lines.drop(1).head.split(' ').map(_.toLong)
    val memo = Array.ofDim[Long](input.length + 1, input.length + 1, 2)

    (1 to input.length).foreach { n =>
      memo(n-1)(n)(0) = input(n-1)
      memo(n-1)(n)(1) = 0
    }

    (2 to input.length).foreach { right =>
      (2 to right).foreach { range =>
        var locMin = Long.MaxValue
        var cost = 0L
        ((right - range + 1) to (right - 1)).reverse.foreach { split =>
          var cand = memo(right - range)(split)(1) + memo(split)(right)(1)
          if (cand < locMin) {
            locMin = cand
            cost = memo(right - range)(split)(0) + memo(split)(right)(0)
          }
        }
        memo(right - range)(right)(0) = cost
        memo(right - range)(right)(1) = locMin + cost
      }
    }

    println(memo(0)(input.length)(1))
  }
}
