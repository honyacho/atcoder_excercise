import scala.collection.mutable.PriorityQueue
import scala.collection.mutable.Set
import scala.util.Sorting

object Main {
  val pq = PriorityQueue[(Long, (Int, Int, Int))]()(scala.math.Ordering.by(v => v._1))
  val lines = scala.io.Source.stdin.getLines.toStream
  val Array(num_x, num_y, num_z, num_k) = lines(0).split(" ").map(_.toLong)
  val xs = lines(1).split(" ").map(_.toLong)
  val ys = lines(2).split(" ").map(_.toLong)
  val zs = lines(3).split(" ").map(_.toLong)
  Sorting.quickSort[Long](xs)(Ordering[Long].reverse)
  Sorting.quickSort[Long](ys)(Ordering[Long].reverse)
  Sorting.quickSort[Long](zs)(Ordering[Long].reverse)
  val checked = Set[(Int, Int, Int)]()
  pq.enqueue((xs(0) + ys(0) + zs(0)) -> (0, 0, 0))

  def main(args: Array[String]) = {
    bfs(num_k)
  }

  def bfs(max: Long = 3000, count: Long = 1): Unit = {
    val (value, (lx, ly, lz))  = pq.dequeue
    println(value)
    if (xs.length > lx+1 && !checked.contains((lx + 1, ly, lz))) {
      checked += ((lx+1, ly, lz))
      pq.enqueue((value - xs(lx) + xs(lx + 1)) -> (lx + 1, ly, lz))
    }
    if (ys.length > ly+1 && !checked.contains((lx, ly+1, lz))) {
      checked += ((lx, ly+1, lz))
      pq.enqueue((value - ys(ly) + ys(ly+1)) -> (lx, ly+1, lz))
    }
    if (zs.length > lz+1 && !checked.contains((lx, ly, lz+1))) {
      checked += ((lx, ly, lz+1))
      pq.enqueue((value - zs(lz) + zs(lz+1)) -> (lx, ly, lz+1))
    }
    if (count < max && (zs.length > lz+1 || ys.length > ly+1 || xs.length > lx+1)) {
      bfs(max, count + 1)
    }
  }
}
