import scala.io.Source
import scala.collection.mutable.Map

object Main {
  val map = Map[(Int, Int, Int)]()

  def main(args: Array[String]) = {
    val lines = Source.stdin.getLines.toStream
    val width = lines.head.toInt
    val Array(num, maxScr) = lines.drop(1).head.split(' ').map(_.toInt)
    val inList = lines.drop(2).take(num).map{ v =>
      val Array(left, right) = v.split(' ').map(_.toInt)
      left -> right
    }.toList

    println(dp(width, inList, 0, maxScr))
  }

  // left 長さ right 重要度
  def dp(num: Int, source: List[(Int, Int)], depth: Int, maxDepth: Int): Int = {
    if (num <= 0) return 0

    var max = 0
    if (depth < maxDepth) {
      source match {
        case (width, weight) :: tail =>
          if (num - width >= 0) {
            // 使うパターン
            val candidate1 = dp(num - width, tail, depth + 1, maxDepth) + weight
            if (candidate1 > max) {
              max = candidate1
            }
          }
          // 使わないパターン
          val candidate2 = dp(num, tail, depth, maxDepth)
          if (candidate2 > max) {
            max = candidate2
          }
        case Nil =>
      }
    }
    max
  }
}
