import scala.io.Source

object Main {
  def main(args: Array[String]) = {
    val lines = Source.stdin.getLines
    val numLine = lines.next.toInt
    val coordinates = lines.take(numLine).map(line => line.split(" ").map(str => str.toDouble)).toArray

    var max = 0.0d

    for {
      i <- 0 to (numLine-1)
      j <- 0 to (numLine-1)
    } {
      val x = coordinates(i)(0) - coordinates(j)(0)
      val y = coordinates(i)(1) - coordinates(j)(1)
      val dist = math.sqrt(x * x + y * y)
      if (max < dist) max = dist
    }

    println(max)
  }
}
