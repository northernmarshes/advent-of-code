use std::fs::read_to_string;

pub fn process_part1(input: &str) -> String {
    let lines = read_lines(input);
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
    result.to_string()
}

pub fn process_part2(input: &str) -> String {
    // let filename = "sample.txt";
    let lines = read_lines(input);
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
        if range[1] >= range[2] && range[0] <= range[3] {
            // println!("The {range:?} ranges overlap.");
            result += 1
        } else {
            // println!("doesn't overlap")
        }
    }
    result.to_string()
}

/// Change text file into an iterator.
pub fn read_lines(name: &str) -> Vec<String> {
    read_to_string(name)
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    // 2-4,6-8
    // 2-3,4-5
    // 5-7,7-9
    // 2-8,3-7
    // 6-6,4-6
    // 2-6,4-8

    #[test]
    fn part1_works() {
        let input = "./sample.txt";
        let result = process_part1(input);
        assert_eq!(result, "2");
    }

    #[test]
    fn part2_works() {
        let input = "./sample.txt";
        let result = process_part2(input);
        assert_eq!(result, "4");
    }
}
