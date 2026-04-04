use std::fs::File;
use std::io::prelude::*;

fn main() {
    let mut f = File::open("sample.txt").expect("file not found");
    let mut contents = String::new();
    f.read_to_string(&mut contents)
        .expect("something wring with the file");
    println!("{}", contents);
}
