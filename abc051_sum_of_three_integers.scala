import scala.io.Source

object Main {
  def main(args: Array[String]) = {
    val lines = Source.stdin.getLines
    val Array(eachMax, sum) = lines.next.split(" ").map(_.toInt)

    var pattern = 0
    for {
      x <- 0 to (math.min(eachMax, sum))
      y <- 0 to (math.min(eachMax, sum - x)) if ((sum - x - y) <= eachMax)
    } {
      pattern = pattern + 1
    }

    println(pattern)
  }
}
