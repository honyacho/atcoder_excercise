import scala.io.Source
import scala.collection.immutable.TreeMap


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

    val numLines = lines.head.toInt
    val data = lines.drop(1).take(numLines).map(line => line.split(" ").map(_.toInt))
      .sortWith((a, b) => a(1) < b(1) || (a(1) == b(1) && a(0) > b(0))).toArray
    val widthMax = data.maxBy(_.apply(0)).apply(0)

    val bit = new BITree(widthMax)
    loop(0, data, bit, 1)
  }

  def loop(index: Int, data: Array[Array[Int]], bit: BITree, max: Int): Unit = {
    val width = data(index)(0)
    val score = bit.max(width-1) + 1
    bit.add(width, score)

    if (index < data.length - 1) {
      loop(index + 1, data, bit, if (score > max) score else max)
    } else {
      println(if (score > max) score else max)
    }
  }
}
