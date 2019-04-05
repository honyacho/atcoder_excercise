import scala.io.Source
import scala.collection.mutable.Map

object Main {
  val memo = Map[String, Int]()

  def main(args: Array[String]) = {
    val lines = Source.stdin.getLines.toStream

    println(dp(lines.head))
  }

  def dp(input: String): Int = {
    val resOpt = memo.get(input)
    if (resOpt.nonEmpty) {
      resOpt.get
    } else {
      var max = 0

      if (input.length >= 3) {
        (0 to input.length - 3).foreach { i =>
          if (input(i) == 'i' && input(i+1) == 'w' && input(i+2) == 'i') {
            val next = dp(input.slice(0, i) + input.slice(i+3, input.length)) + 1
            if (next > max) max = next
          }
        }
      }

      max
    }
  }
}
