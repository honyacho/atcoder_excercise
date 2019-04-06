import scala.collection.mutable.PriorityQueue
import scala.collection.mutable.Set

object Main {

  def main(args: Array[String]) = {
    val lines = scala.io.Source.stdin.getLines.toStream

    val Array(num_x, num_y, num_z, num_k) = lines(0).split(" ").map(_.toLong)
    var xs = lines(1).split(" ").map(_.toLong)
    var ys = lines(2).split(" ").map(_.toLong)
    var zs = lines(3).split(" ").map(_.toLong)
    java.util.Arrays.sort(xs)
    java.util.Arrays.sort(ys)
    java.util.Arrays.sort(zs)
    xs = xs.reverse
    ys = ys.reverse
    zs = zs.reverse

    var x = xs(0)
    var y = ys(0)
    var z = zs(0)

    var cnt = 0L
    val pq = PriorityQueue[((Long, Char), (Int, Int, Int))]()(scala.math.Ordering.by((v: ((Long, Char), (Int, Int, Int))) => v._1))
    pq.enqueue((x + y + z, 'w') -> (0, 0, 0))
    dfs(pq, xs, ys, zs, num_k)
  }

  def dfs(
    q: PriorityQueue[((Long, Char), (Int, Int, Int))], 
    xs: Array[Long], 
    ys: Array[Long], 
    zs: Array[Long], 
    max: Long = 3000, 
    count: Long = 1, 
    checked: Set[(Int, Int, Int)] = Set()): Unit = {
    val ((value, c), (lx, ly, lz))  = q.dequeue
    println(value)
    if (xs.length > lx+1 && !checked.contains((lx + 1, ly, lz))) {
      checked += ((lx + 1, ly, lz))
      q.enqueue((value - xs(lx) + xs(lx + 1), 'x') -> (lx + 1, ly, lz))
    }
    if (ys.length > ly+1 && !checked.contains((lx, ly+1, lz))) {
      checked += ((lx, ly+1, lz))
      q.enqueue((value - ys(ly) + ys(ly+1), 'y') -> (lx, ly+1, lz))

    }
    if (zs.length > lz+1 && !checked.contains((lx, ly, lz+1))) {
      checked += ((lx, ly, lz+1))
      q.enqueue((value - zs(lz) + zs(lz+1), 'z') -> (lx, ly, lz+1))
    }

    if (count < max && (zs.length > lz+1 || ys.length > ly+1 || xs.length > lx+1)) {
      dfs(q, xs, ys, zs, max, count + 1, checked)
    }
  }
}
