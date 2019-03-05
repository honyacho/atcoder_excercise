import scala.io.Source

object Main {
  def main(args: Array[String]) = {
    val lines = Source.stdin.getLines.toStream
    val Array(numLines, linesPerPage, pageToShow) = lines.head.split(" ").map(_.toInt)

    lines.drop(1).drop(linesPerPage * (pageToShow - 1)).take(linesPerPage).foreach(println _)
  }
}
