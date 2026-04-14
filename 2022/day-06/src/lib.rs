use std::{collections::HashSet, fs::read_to_string};

pub fn process_part1(input: &str) -> String {
    let line: String = read_lines(input);
    let mut result: u32 = 0;
    let mut letters: Vec<char> = Vec::new();

    for char in line.chars() {
        letters.push(char);
    }

    for (index, _letter) in letters.iter().enumerate() {
        let mut set = HashSet::new();
        set.insert(&letters[index]);
        set.insert(&letters[index + 1]);
        set.insert(&letters[index + 2]);
        set.insert(&letters[index + 3]);
        if set.len() == 4 {
            result = index as u32 + 4;
            break;
        }
    }

    result.to_string()
}

pub fn process_part2(input: &str) -> String {
    let line: String = read_lines(input);
    let mut result: u32 = 0;
    let mut letters: Vec<char> = Vec::new();

    for char in line.chars() {
        letters.push(char);
    }

    for (index, _letter) in letters.iter().enumerate() {
        let mut set = HashSet::new();
        let mut n = 0;
        while n < 14 {
            set.insert(&letters[index + n]);
            n += 1;
        }
        if set.len() == 14 {
            result = index as u32 + 14;
            break;
        }
    }

    result.to_string()
}

// parse the input
pub fn read_lines(name: &str) -> String {
    read_to_string(name).unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;

    // mjqjpqmgbljsphdztnvjfqwrcgsmlb
    // bvwbjplbgvbhsrlpgdmjqwftvncz
    // nppdvjthqldpwncqszvftbrmjlhg
    // nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
    // zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw

    #[test]
    fn part1_works_01() {
        let input = "./sample_1.txt";
        let result = process_part1(input);
        assert_eq!(result, "7");
    }

    #[test]
    fn part1_works_02() {
        let input = "./sample_2.txt";
        let result = process_part1(input);
        assert_eq!(result, "5");
    }

    #[test]
    fn part1_works_03() {
        let input = "./sample_3.txt";
        let result = process_part1(input);
        assert_eq!(result, "6");
    }

    #[test]
    fn part1_works_04() {
        let input = "./sample_4.txt";
        let result = process_part1(input);
        assert_eq!(result, "10");
    }

    #[test]
    fn part1_works_05() {
        let input = "./sample_5.txt";
        let result = process_part1(input);
        assert_eq!(result, "11");
    }

    // part 2

    #[test]
    fn part2_works_01() {
        let input = "./sample_1.txt";
        let result = process_part2(input);
        assert_eq!(result, "19");
    }

    #[test]
    fn part2_works_02() {
        let input = "./sample_2.txt";
        let result = process_part2(input);
        assert_eq!(result, "23");
    }

    #[test]
    fn part2_works_03() {
        let input = "./sample_3.txt";
        let result = process_part2(input);
        assert_eq!(result, "23");
    }

    #[test]
    fn part2_works_04() {
        let input = "./sample_4.txt";
        let result = process_part2(input);
        assert_eq!(result, "29");
    }

    #[test]
    fn part2_works_05() {
        let input = "./sample_5.txt";
        let result = process_part2(input);
        assert_eq!(result, "26");
    }
}
