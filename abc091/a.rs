use std::io;
use std::str::FromStr;


fn main() {
    let stdin = io::stdin();
    let mut buf = String::new();
    stdin.read_line(&mut buf).ok();
    let mut it = buf.split_whitespace().map(|n| usize::from_str(n).unwrap());
    let (a, b, c) = (it.next().unwrap(), it.next().unwrap(), it.next().unwrap());
    if a + b >= c {
        println!("Yes");
    } else {
        println!("No");
    }
}
