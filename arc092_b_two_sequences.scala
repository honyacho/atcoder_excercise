import scala.io.Source
object Main {
  def binarySearch(arr: Array[Int], value: Int): Int = {
    var i = 0
    var j = arr.length
    var half = (i+j)/2
    while (i < j) {
      if (arr(half) >= value) j = half else i = half+1
      half = (i+j)/2
    }
    i
  }

  def main(args: Array[String]) = {
    val lines = Source.stdin.getLines
    val N = lines.next.toInt
    val A = lines.next.split(" ").map(_.toInt)
    val B = lines.next.split(" ").map(_.toInt)

    var res = 0
    for (i <- (0 to 29).reverse) {
      val (higher, lower) = (1<<(i+1), 1<<i)
      for (j <- 0 until N) {
        A(j) = A(j) % higher
        B(j) = B(j) % higher
      }
      java.util.Arrays.sort(B)
      var loc_sum = 0
      for (k <- 0 until N) {
        if (lower-A(k) >= 0) {
          loc_sum += binarySearch(B, higher-A(k))
          loc_sum -= binarySearch(B, lower-A(k))
        } else {
          loc_sum += binarySearch(B, higher-A(k))
          loc_sum += binarySearch(B, higher)
          loc_sum -= binarySearch(B, higher + lower - A(k))
        }
      }
      res += lower*(loc_sum&1)
    }
    println(res)
  }
}
