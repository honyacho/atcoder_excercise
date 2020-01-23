import scala.io.Source
import scala.collection.mutable.{ SortedSet => MSet }
import scala.collection.mutable.PriorityQueue

object Main {
  def main(args: Array[String]): Unit = {
    val lines = Source.stdin.getLines.toStream
    val Array(n, q) = lines.head.split(" ").map(_.toInt)
    val pq = new PriorityQueue[(Double, Char, Int)]()

    lines.drop(1).take(n).foreach { row =>
      val Array(s,t,x) = row.split(" ")
      pq.enqueue((-(s.toDouble - 0.5 - x.toDouble), 's', x.toInt))
      pq.enqueue((-(t.toDouble - 0.75 - x.toDouble), 'e', x.toInt))
    }
    lines.drop(1+n).take(q).zipWithIndex.foreach { case (row, i) =>
      pq.enqueue(((-row.toDouble), 'p', i))
    }

    val res = new Array[Int](q)

    val st = MSet[Int]()
    while (pq.length > 0) {
      val (tim, typ, num) = pq.dequeue()
      if (typ == 's') {
        st += num
      }
      if (typ == 'e') {
        st -= num
      }
      if (typ == 'p') {
        res(num) = if (st.size == 0) -1 else {
          st.iterator.next
        }
      }
    }
    res.foreach(println)
  }
}
