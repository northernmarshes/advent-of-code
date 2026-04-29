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

// pub fn process_part2(input: &str) -> String {
//     result.to_string()
// }

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

    // #[test]
    // fn part2_works() {
    //     let input = "./sample.txt";
    //     let result = process_part2(input);
    //     assert_eq!(result, "");
    // }
}
