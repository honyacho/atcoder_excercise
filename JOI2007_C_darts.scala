object Main {
  def main(args: Array[String]) = {
    val lines = Source.stdin.getLines.toStream
    val Array(height, width) = lines.head.split(" ").map(_.toInt)

  }
}
