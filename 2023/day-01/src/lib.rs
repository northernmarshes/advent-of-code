use regex::Regex;
use std::fs::read_to_string;

pub fn process_part1(input: &str) -> String {
    let mut result: u32 = 0;
    let lines = read_lines(input);
    for line in lines {
        let mut digits: Vec<u32> = Vec::new();
        for n in line.chars() {
            if n.is_numeric() {
                let num: u32 = n as u32 - 0x30;
                digits.push(num);
            }
        }
        if !digits.is_empty() {
            let digits_len = digits.len() - 1;
            let first = digits[0];
            let last = digits[digits_len];
            println!("first: {first} and last: {last}");
            result += first * 10 + last;
        }
        println!("{digits:?}");
    }
    result.to_string()
}

pub fn process_part2(input: &str) -> String {
    let mut result: u32 = 0;
    let mut numbers: Vec<Vec<u32>> = Vec::new();
    let lines = read_lines(input);
    let re = Regex::new(r"\d|(?:one|two|three|four|five|six|seven|eight|nine)").unwrap();

    for line in lines {
        let mut line_nums: Vec<u32> = Vec::new();
        let l = line.as_str();
        // let n: Vec<&str> = re.find_iter(l).map(|m| m.as_str()).collect();
        let n: Vec<&str> = re.find_iter(l).map(|m| m.as_str()).collect();
        // println!("{n:?}");
        for num in n {
            let letters: Vec<char> = num.chars().collect();
            if letters[0].is_numeric() {
                let digit = letters[0] as u32 - 0x30;
                line_nums.push(digit);
                // println!("{digit}");
            } else {
                let digit: u32 = match num {
                    "one" => 1,
                    "two" => 2,
                    "three" => 3,
                    "four" => 4,
                    "five" => 5,
                    "six" => 6,
                    "seven" => 7,
                    "eight" => 8,
                    "nine" => 9,
                    _ => 0,
                };
                line_nums.push(digit);
            }
        }
        numbers.push(line_nums.clone());
    }
    // result.to_string()
    // println!("{numbers:?}");
    for n in numbers {
        result += n[0] * 10 + n[n.len() - 1];
    }
    result.to_string()
}

// parse the input
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

    // 1abc2
    // pqr3stu8vwx
    // a1b2c3d4e5f
    // treb7uchet

    #[test]
    fn part1_works() {
        let input = "./sample.txt";
        let result = process_part1(input);
        assert_eq!(result, "142");
    }

    // two1nine
    // eightwothree
    // abcone2threexyz
    // xtwone3four
    // 4nineeightseven2
    // zoneight234
    // 7pqrstsixteen

    #[test]
    fn part2_works() {
        let input = "./sample_02.txt";
        let result = process_part2(input);
        assert_eq!(result, "281");
    }
}
