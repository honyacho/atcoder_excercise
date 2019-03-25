object Main {
  def main(args: Array[String]) = {
    val lines = scala.io.Source.stdin.getLines.toStream
    val Array(numLines, limit) = lines.head.split(" ").map(_.toInt)
    val scores = 0 +: lines.drop(1).map(_.toInt).toArray
    val doubles = Array.fill((numLines+1)*(numLines+1))(0)

    var max = 0
    for {
      throw1 <- scores
      throw2 <- scores
    } {
      doubles(i) = throw1 + throw2
      i += 1
    }
    java.util.Arrays.sort(doubles)

    for (double <- doubles) {
      var cand = double
      if (cand <= limit) {
        if (cand < limit) cand = cand + bin(0, doubles.length, limit - cand, doubles)
        if (cand > max) max = cand
      }
    }

    println(max)
  }

  def bin(from: Int, to: Int, limit: Int, array: Array[Int]): Int = {
    val half = (from + to) / 2
    if (from == half) return array(from)
    val cand = array(half)
    if (cand <= limit) bin(half, to, limit, array) else bin(from, half, limit, array)
  }
}
