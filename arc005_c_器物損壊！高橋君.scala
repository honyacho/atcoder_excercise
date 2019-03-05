import scala.io.Source
import scala.collection.mutable.{ Set => MSet }
import scala.collection.mutable.Queue

object Main {
  def main(args: Array[String]) = {
    val lines = Source.stdin.getLines.toStream
    val Array(height, width) = lines.head.split(" ").map(_.toInt)
    val map = lines.drop(1).take(height).reduce(_ + _).toCharArray
    val queue = Array(Queue[(Int, Int)](), Queue[(Int, Int)](), Queue[(Int, Int)]())
    val isVisited = MSet[(Int, Int)]()

    val start = (for {
      j <- 0 to (height - 1)
      i <- 0 to (width - 1) if (map(j * width + i) == 's')
    } yield (i, j)).head
    queue(0).enqueue(start)

    if (bfs(map, isVisited, queue, 0, width, height)) {
       println("YES")
    } else {
       println("NO")
    }
  }

  val adjust = Array((0, 1), (1, 0), (-1, 0), (0, -1))

  def bfs(map: Array[Char], isVisited: MSet[(Int, Int)], queueArr: Array[Queue[(Int, Int)]], break: Int, width: Int, height: Int): Boolean = {
    if (break >= 3) {
      false
    } else if (queueArr(break).isEmpty) {
      bfs(map, isVisited, queueArr, break+1, width, height)
    } else {
      val (posX, posY) = queueArr(break).dequeue
      isVisited += ((posX, posY))

      if (map(posY * width + posX) == 'g') {
        true
      } else {
        adjust.foreach { case (dx, dy) =>
          if ((posX + dx >= 0) && (posX + dx < width) && (posY + dy >= 0) && (posY + dy < height)) {
            val nextBreak = (if (map((posY + dy) * width + posX + dx) == '#') 1 else 0) + break
            if (!isVisited.contains((posX + dx, posY + dy)) && nextBreak <= 2) {
              queueArr(nextBreak).enqueue((posX + dx, posY + dy))
            }
          }
        }
        bfs(map, isVisited, queueArr, break, width, height)
      }
    }
  }
}
