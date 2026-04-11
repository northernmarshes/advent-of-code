use std::fs::read_to_string;

pub fn process_part1(input: &str) -> String {
    let lines = read_lines(input);
    let result = String::from("");
    let mut crate_lines: Vec<String> = Vec::new();
    let mut stacks_count: usize = 0;
    let mut stacks_line_length = 0;
    let mut indexes: Vec<usize> = vec![1];
    let mut stacks: Vec<Vec<char>> = Vec::new();

    // separate lines with crate names and count the stacks
    for line in lines {
        if line.contains("[") {
            crate_lines.push(line.clone());
            if line.len() > stacks_count {
                stacks_count = (line.len() + 1) / 4;
                stacks_line_length = line.len();
            }
        }
    }

    // find indexes of each stack
    for _stack in 0..stacks_count - 1 {
        let line = indexes[indexes.len() - 1] as usize;
        indexes.push(line + 4);
    }

    // construct vectors with crate stacks
    for index in &indexes {
        let mut stack: Vec<char> = Vec::new();
        for line in &crate_lines {
            let i: usize = *index;
            let crate_name = line.chars().nth(i).unwrap();
            if crate_name.is_alphabetic() {
                stack.push(crate_name);
            }
        }
        stacks.push(stack);
    }

    println!("{stacks:?}");
    println!("Stacks counts is {stacks_count}");
    println!("Stacks indexes are {stacks_line_length}");
    // println!("{crate_lines:?}");
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

    //     [D]
    // [N] [C]
    // [Z] [M] [P]
    //  1   2   3
    //
    // move 1 from 2 to 1
    // move 3 from 1 to 3
    // move 2 from 2 to 1
    // move 1 from 1 to 2"

    #[test]
    fn part1_works() {
        let input = "./sample.txt";
        let result = process_part1(input);
        assert_eq!(result, "CMZ");
    }
}
