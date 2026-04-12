use std::{fs::read_to_string, vec};

pub fn process_part1(input: &str) -> String {
    let mut result = String::from("");
    let (mut stacks, instructions) = parse_crates_and_instructions(input);

    // move crates with CM9000
    for instruction in instructions {
        stacks = move_crates_with_cratemover_9000(stacks, instruction);
    }

    // check what's on top
    for stack in stacks {
        let top_crate = stack[stack.len() - 1];
        result.push(top_crate);
    }

    result
}

pub fn process_part2(input: &str) -> String {
    let mut result = String::from("");
    let (mut stacks, instructions) = parse_crates_and_instructions(input);

    // move crates with CM9001
    for instruction in instructions {
        stacks = move_crates_with_cratemover_9001(stacks, instruction);
    }

    // check what's on top
    for stack in stacks {
        let top_crate = stack[stack.len() - 1];
        result.push(top_crate);
    }

    result
}

pub fn parse_crates_and_instructions(input: &str) -> (Vec<Vec<char>>, Vec<Vec<usize>>) {
    let lines = read_lines(input);
    let mut crate_lines: Vec<String> = Vec::new();
    let mut instruction_lines: Vec<String> = Vec::new();
    let mut stacks_count: usize = 0;
    let mut indexes: Vec<usize> = vec![1];
    let mut stacks: Vec<Vec<char>> = Vec::new();
    let mut instructions: Vec<Vec<usize>> = Vec::new();

    // separate lines with crate names and count the stacks
    for line in lines {
        if line.contains("[") {
            crate_lines.push(line.clone());
            if line.len() > stacks_count {
                stacks_count = (line.len() + 1) / 4;
            }
        } else if line.contains("move") {
            instruction_lines.push(line.clone());
        }
    }

    // find indexes of each stack
    for _stack in 0..stacks_count - 1 {
        let line = indexes[indexes.len() - 1] as usize;
        indexes.push(line + 4);
    }

    // parse instructions to vectors
    for line in &instruction_lines {
        let mut instruction: Vec<usize> = Vec::new();
        for char in line.chars() {
            if char.is_numeric() {
                let inst = char as usize - '0' as usize;
                instruction.push(inst);
            }
        }
        // walkaround for numbers of operations larger then 9
        if instruction.len() > 3 {
            let decimal = instruction[0] * 10;
            instruction[1] += decimal;
            instruction.remove(0);
            instructions.push(instruction);
        } else {
            instructions.push(instruction);
        }
    }

    // reverse the lines
    crate_lines.reverse();

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
    (stacks, instructions)
}

// part 1 crate movement logic
pub fn move_crates_with_cratemover_9000(
    stack: Vec<Vec<char>>,
    moves: Vec<usize>,
) -> Vec<Vec<char>> {
    let mut boxes = stack;
    let mut layers_to_move = moves[0];
    let crate_to_move: usize = moves[1] - 1;
    let destination_stack = moves[2] - 1;

    while 0 < layers_to_move {
        let last_crate: char = boxes[crate_to_move].pop().unwrap();
        layers_to_move -= 1;
        boxes[destination_stack].push(last_crate);
    }

    boxes
}

// part 2 crate movement logic
pub fn move_crates_with_cratemover_9001(
    stack: Vec<Vec<char>>,
    moves: Vec<usize>,
) -> Vec<Vec<char>> {
    let mut boxes = stack;
    let mut layers_to_move = moves[0];
    let crate_to_move: usize = moves[1] - 1;
    let destination_stack = moves[2] - 1;
    let mut grab: Vec<char> = Vec::new();

    while 0 < layers_to_move {
        let last_crate: char = boxes[crate_to_move].pop().unwrap();
        layers_to_move -= 1;
        grab.push(last_crate);
    }

    grab.reverse();

    for portion in grab {
        boxes[destination_stack].push(portion);
    }

    boxes
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

    #[test]
    fn move_crates_works() {
        let crates = vec![vec!['A', 'B', 'C'], vec!['C', 'D', 'F']];
        let crates_after = vec![vec!['A', 'B', 'C', 'F'], vec!['C', 'D']];
        let instructions: Vec<usize> = vec![1, 2, 1];
        let result = move_crates_with_cratemover_9000(crates, instructions);
        assert_eq!(result, crates_after);
    }

    #[test]
    fn move_crates_more_then_9() {
        let crates = vec![
            vec!['A', 'B', 'C'],
            vec![
                'C', 'D', 'F', 'Z', 'G', 'H', 'E', 'B', 'W', 'N', 'Q', 'L', 'P', 'E',
            ],
        ];
        let crates_after = vec![
            vec![
                'A', 'B', 'C', 'E', 'P', 'L', 'Q', 'N', 'W', 'B', 'E', 'H', 'G', 'Z', 'F',
            ],
            vec!['C', 'D'],
        ];
        let instructions: Vec<usize> = vec![12, 2, 1];
        let result = move_crates_with_cratemover_9000(crates, instructions);
        assert_eq!(result, crates_after);
    }
}
