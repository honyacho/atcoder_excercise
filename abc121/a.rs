fn read<T: std::str::FromStr>() -> T {
  let mut s = String::new();
  std::io::stdin().read_line(&mut s).ok();
  s.trim().parse().ok().unwrap()
}

fn read_vec<T: std::str::FromStr>() -> Vec<T> {
  let mut s = String::new();
  std::io::stdin().read_line(&mut s).ok();
  s.trim().split_whitespace()
    .map(|e| e.parse().ok().unwrap()).collect()
}

fn main() {
  let size: Vec<i32> = read_vec();
  let white_line: Vec<i32> = read_vec();
  println!("{}", size[0]*size[1] - (white_line[0]*size[1] + white_line[1]*size[0] - white_line[0]*white_line[1]));
}
