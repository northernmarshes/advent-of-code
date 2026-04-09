use std::fs::read_to_string;

fn main() {
    let filename = "sample.txt";
    // let filename = "input.txt";
    let lines = read_lines(filename);
    for line in &lines {
        println!("{line}");
    }
}

/// Change text file into an iterator.
fn read_lines(name: &str) -> Vec<String> {
    read_to_string(name)
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}
