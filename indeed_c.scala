import scala.io.Source
import scala.collection.mutable.SortedSet

class BITree(size: Int) {
  val behind = new Array[Int](size + 1)

  def max(value: Int): Int = {
    if (value == 0) return 0
    val beh = behind(value)
    val curMax = max(value - (value & (-value)))
    if (beh > curMax) beh else curMax
  }

  def add(value: Int, score: Int): Unit = {
    if (value >= behind.length) return;
    if (score > behind(value)) behind(value) = score
    add(value + (value & (-value)), score)
  }

  override def toString: String = behind.toList.toString()
}

object Main {
  def main(args: Array[String]) = {
    val lines = Source.stdin.getLines.toStream
    val Array(nums, range) = lines.head.split(" ").map(_.toInt)

    val bit = new BITree(200000)

    val array = lines.drop(1).head.split(" ").map(_.toInt).toArray
    array.zipWithIndex.foreach { case (num, i) =>
      bit.add(19999 - i, num)
      if (i >= (range - 1)) {
        println(bit.max(19999 - (i - range)))
      }
    }
  }
}
