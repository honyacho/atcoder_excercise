import scala.io.Source

object Main {
  def main(args: Array[String]) = {
    val lines = Source.stdin.getLines.toStream

    val str = lines.head
    if (str.length > 1) {
      println(str.take(str.length - 1))
    } else {
      val char = str.toCharArray.head
      if (char == 'a') {
        println("-1")
      } else {
        println((char.toInt - 1).toChar.toString)
      }
    }
  }
}
