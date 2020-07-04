import scala.io.Source

object Main {
  def main(args: Array[String]) = {
    val lines = Source.stdin.getLines.toStream
    val Array(len, maxSwap) = lines.head.split(" ").map(_.toInt)
    println(loop(lines.drop(1).head, maxSwap, 0, lines.drop(1).head))
  }

  def loop(original: String, maxSwap: Int, cur: Int, result: String): String = {
    if (cur >= original.length) return result

    val candidates = result.zipWithIndex.slice(cur + 1, original.length)
      .filter { case (char, i) => char < result(cur) }.sortBy(_._1)
    val next = candidates.view
      .map { case (char, i) => result.updated(cur, char).updated(i, result(cur)) }
      .find( candidate => diff(original, candidate) <= maxSwap ).getOrElse(result)

    loop(original, maxSwap, cur + 1, next)
  }

  def diff(str1: String, str2: String): Int = (0 to (str1.length - 1)).filter( i => str1(i) != str2(i)).length
}
