use std::fs::read_to_string;

pub fn process_part1(input: &str) {}
pub fn process_part2(input: &str) {}

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

    // mjqjpqmgbljsphdztnvjfqwrcgsmlb

    #[test]
    fn part1_works() {
        let input = "./sample.txt";
        let result = process_part1(input);
        assert_eq!(result, "7");
    }
}
