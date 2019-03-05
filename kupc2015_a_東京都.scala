import scala.io.Source
import scala.collection.mutable.{ Set => MSet }

object Main {
  def main(args: Array[String]) = {
    val lines = Source.stdin.getLines.toStream

    val numLines = lines.head.toInt
    val reg = "(tokyo|kyoto)".r
    lines.drop(1).take(numLines).foreach { line =>
      println(reg.findAllIn(line).length)
    }
  }
}
