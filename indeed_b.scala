import scala.io.Source

object Main {
  def main(args: Array[String]) = {
    val lines = Source.stdin.getLines.toStream
    val Array(numRooms, numInit) = lines.head.split(" ").map(_.toInt)

    var resv = lines.drop(1).take(numInit).map { _.split(" ").map(_.toLong) }
    val numReq = lines.drop(numInit + 1).head.toInt

    lines.drop(numInit + 2).take(numReq).map(_.split(" ").map(_.toLong)).foreach { kukan1 =>
      var availability = true
      resv.foreach { kukan2 =>
        availability = availability &&
          !(kukan2(0) <= kukan1(0) && kukan1(0) <= kukan2(1) ) &&
          !(kukan2(0) <= kukan1(1) && kukan1(1) <= kukan2(1) ) &&
          !(kukan2(0) >= kukan1(0) && kukan1(1) >= kukan2(1) )
      }
      println(if (availability) "OK" else "NG")
      if (availability) resv = resv :+ kukan1
    }
  }
}
