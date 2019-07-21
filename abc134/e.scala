import scala.collection.mutable.TreeSet
import scala.io.Source
object Main {
  val lines = Source.stdin.getLines.toStream.map(_.toInt)
  val n = lines.head
  val inArr = lines.tail.toArray

  def main(args: Array[String]) = {
    val st = TreeSet[(Int, Int)]()
    var color = 1

    for (i <- 0 until n) {
      val it = st.iteratorFrom((-(inArr(i)-1), 0))
      if (it.hasNext) {
        val (locMax, num) = it.next
        st -= ((locMax, num))
        st += ((-inArr(i), num))
      } else {
        st += ((-inArr(i), color))
        color = color+1
      }
    }
    println(st.size)
  }
}
