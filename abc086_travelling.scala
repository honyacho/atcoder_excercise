import scala.io.Source

object Main {
  def main(args: Array[String]) = {
    val lines = Source.stdin.getLines
    val numLine = lines.next.toInt
    val numbers = lines.take(numLine).toSeq.map(l => l.split(" ").map(_.toInt).toSeq)

    val res = (Seq(0,0,0) +: numbers).take(numLine).zip(numbers).map {
      case (prev, next) => {
        val time = next(0) - prev(0)
        val distance = math.abs(next(1) - prev(1)) + math.abs(next(2) - prev(2))
        (time % 2) == (distance % 2) && (distance <= time)
      }
    }.reduce(_ && _)
    println(if (res) "Yes" else "No")
  }
}
