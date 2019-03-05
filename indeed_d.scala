import scala.io.Source
import scala.collection.mutable.SortedSet

object Main {
  def main(args: Array[String]) = {
    val lines = Source.stdin.getLines.toStream
    val Array(nums, range) = lines.head.split(" ").map(_.toInt)

  }
}
