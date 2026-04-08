use std::fs::read_to_string;

fn main() {
    let filename = "sample.txt";
    let lines = read_lines(filename);
    let mut ranges: Vec<Vec<Vec<&str>>> = Vec::new();

    for line in &lines {
        let sentence = line.as_str();
        let mut single_pair: Vec<Vec<&str>> = Vec::new();
        let words: Vec<&str> = sentence.split(',').collect();
        let word_01: Vec<&str> = words[0].split('-').collect();
        let word_02: Vec<&str> = words[1].split('-').collect();
        single_pair.push(word_01);
        single_pair.push(word_02);
        ranges.push(single_pair);
    }

    println!("{ranges:?}");
}

/// Change text file into an iterator.
fn read_lines(name: &str) -> Vec<String> {
    read_to_string(name)
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}
