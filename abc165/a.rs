use std::io;
use std::str::FromStr;

fn main() {
    let stdin = io::stdin();
    let mut buf = String::new();
    stdin.read_line(&mut buf).ok();
    buf.pop();
    let K = i64::from_str(&buf).unwrap();
    buf.clear();
    stdin.read_line(&mut buf).ok();
    let mut it = buf.split_whitespace().map(|n| i64::from_str(n).unwrap());
    let (A, B) = (it.next().unwrap(), it.next().unwrap());
    for i in A..(B+1) {
        if i % K == 0 {
            println!("OK");
            return ();
        }
    }
    println!("NG");
}
