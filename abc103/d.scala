import scala.io.Source
import scala.collection.mutable.{ Set => MSet }

object Main {
  def main(args: Array[String]) = {
    val lines = Source.stdin.getLines.toStream
    val Array(numIslands, numReqs) = lines.head.split(" ").map(_.toInt)
    val reqs = lines.drop(1).take(numReqs).map{ row => val Array(l, r) = row.split(" "); l.toInt -> r.toInt }

    val initial = reqs.foldLeft(Map[Int, List[(Int, Int)]]()) { (map, elem) =>
      val (left, right) = elem
      (left to (right - 1)).foldLeft(map) { (mp, i) =>
        val lst = mp.getOrElse(i, Nil)
        mp.updated(i, (left -> right) :: lst)
      }
    }

    loop(initial.toList.sortBy(_._2.length).reverse)
  }

  def loop(list: List[(Int, List[(Int, Int)])], cnt: Int = 0): Unit = {
    list match {
      case (_, lst) :: rest =>
        if (lst.isEmpty) {
          println(cnt)
        } else {
          val toRem = lst.toSet
          val next = rest.map(v => (v._1, v._2.filter(!toRem.contains(_)))).view.sortBy(_._2.length).reverse.toList
          loop(next, cnt+1)
        }
      case Nil =>
        println(cnt)
    }
  }
}
