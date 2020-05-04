use std::io;
use std::str::FromStr;

fn main() {
    let stdin = io::stdin();
    let mut buf = String::new();
    stdin.read_line(&mut buf).ok();
    buf.pop();
    let X = i64::from_str(&buf).unwrap();
    let mut money = 100;
    let mut cnt = 1;
    loop {
        money = money + (money/100);
        if money >= X {
            println!("{}", cnt);
            return ();
        }
        cnt += 1;
    }
}
