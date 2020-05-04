use std::io;
use std::str::FromStr;
use std::iter::Map;
use std::str::SplitWhitespace;

fn split_to_i64<'r>(buf: &'r String) -> Map<SplitWhitespace, impl FnMut(&'r str) -> i64> {
    let mp = buf
        .split_whitespace()
        .map(|n| i64::from_str(n).unwrap())
        .into_iter();

    return mp;
}

fn get_int() -> i64 {
    let stdin = io::stdin();
    let mut buf = String::new();
    stdin.read_line(&mut buf);
    buf.pop();
    return i64::from_str(&buf).unwrap();
}

fn get_int_itr<'r>(buf: &'r mut String) -> Map<SplitWhitespace, impl FnMut(&'r str) -> i64> {
    let stdin = io::stdin();
    stdin.read_line(buf);
    return split_to_i64(buf);
}

fn main() {
    let stdin = io::stdin();
    let mut buf = String::new();
    stdin.read_line(&mut buf);
    buf.pop();
    let mut it = split_to_i64(&buf);
    let N = it.next().unwrap();
    let K = it.next().unwrap();
    let mut friends: Vec<i32> = Vec::with_capacity(101);
    for i in 0..101 {
        friends.push(0);
    }
    for i in 0..K {
        let mut buf1 = String::new();
        let d = get_int();
        let mut it = get_int_itr(&mut buf1);
        for j in 0..d {
            let id = it.next().unwrap();
            // println!("{}", id);
            friends[id as usize] += 1;
        }
    }
    let mut res = 0;
    for i in 1..(N+1) {
        if friends[i as usize] == 0 {
            res += 1;
        }
    }
    println!("{}", res);
}
