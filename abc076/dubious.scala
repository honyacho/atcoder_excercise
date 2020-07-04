import scala.io.Source

object Main {
  def main(args: Array[String]) = {
    val lines = Source.stdin.getLines.toStream

    val str = lines.head.replace("?", ".")
    val target = lines.drop(1).head

    val res = (0 to (str.length - target.length)).flatMap { n =>
      // println(str.slice(n, n + target.length))
      str.slice(n, n + target.length).r.findFirstIn(target).map(_ => n)
    }

    if (res.nonEmpty) {
      val posLast = res.last
      println(str.slice(0, res.last).replace(".", "a") + target + str.slice(res.last + target.length, str.length).replace(".", "a"))
    } else {
      println("UNRESTORABLE")
    }
  }
}
