use std::fs::read_to_string;

fn main() {
    let filename = "input.txt";
    let lines = read_lines(filename);
    let mut ranges: Vec<Vec<Vec<&str>>> = Vec::new();
    let mut ranges_int: Vec<Vec<i32>> = Vec::new();
    let mut result: u32 = 0;

    // parse numbers to vectors
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

    // change type to integer
    for range in ranges {
        let number_01 = range[0][0].parse::<i32>().unwrap();
        let number_02 = range[0][1].parse::<i32>().unwrap();
        let number_03 = range[1][0].parse::<i32>().unwrap();
        let number_04 = range[1][1].parse::<i32>().unwrap();
        let ints: Vec<i32> = vec![number_01, number_02, number_03, number_04];
        ranges_int.push(ints);
    }

    // calculate if ranges contsin one another
    for range in ranges_int {
        if range[0] <= range[2] && range[1] >= range[3] {
            // println!("the left one contains the right one {range:?}");
            result += 1
        } else if range[0] >= range[2] && range[3] >= range[1] {
            // println!("the right one contains the left one {range:?}");
            result += 1
        } else {
            // println!("none contains the other one")
        }
    }
    println!("In {result} assignment pairs one range fully contains the other.")
}

/// Change text file into an iterator.
fn read_lines(name: &str) -> Vec<String> {
    read_to_string(name)
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}
