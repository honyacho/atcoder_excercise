use std::io::{self, Read};

fn main() -> () {
  let mut buffer = String::new();
  io::stdin().read_to_string(&mut buffer);
  let arr: Vec<&str> = buffer.split(' ').collect();
  println!("{:?}", arr);
}
