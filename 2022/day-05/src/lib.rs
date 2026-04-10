use std::fs::read_to_string;

pub fn process_part1(input: &str) -> String {
    let lines = read_lines(input);
    // let boxes: Vec<Vec<char>> = Vec::new();
    let result = String::from("");

    for line in &lines {
        let mut box_lines: Vec<&String> = Vec::new();
        if line.contains("[") {
            box_lines.push(line);
            println!("{line}");
        }
    }
    result
}

pub fn process_part2() {}

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
    const INPUT: &str = "
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2";

    #[test]
    fn part1_works() {
        let result = process_part1(INPUT);
        assert_eq!(result, "CMZ");
    }
}
