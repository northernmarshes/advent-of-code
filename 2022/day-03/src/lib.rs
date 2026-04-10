use common_substrings::get_substrings;
use std::fs::read_to_string;

pub fn process_part1(input: &str) -> String {
    let mut result: u32 = 0;
    let lines: Vec<String> = read_lines(input);
    let mut common_items: Vec<char> = Vec::new();
    let priorities: Vec<char> = vec![
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    ];

    // Find the common item in both compartments.
    for line in &lines {
        let (first_half, second_half) = line.split_at(line.len() / 2);
        let rucksacks: Vec<&str> = vec![first_half, second_half];
        let result_substrings = get_substrings(rucksacks, 2, 1);
        let item: char = result_substrings[0].name.chars().next().clone().unwrap();
        common_items.push(item);
    }

    // Calculate the result by adding corresponding indexes.
    for item in common_items {
        let priority: u32 = priorities.iter().position(|&x| x == item).unwrap() as u32;
        result += priority + 1;
    }

    result.to_string()
}

pub fn process_part2(input: &str) -> String {
    let mut result: u32 = 0;
    let mut lines: Vec<String> = read_lines(input);
    let mut common_items: Vec<char> = Vec::new();
    let mut elf_groups: Vec<Vec<String>> = Vec::new();
    let priorities: Vec<char> = vec![
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    ];

    // Group elves into groups of three.
    for _num in 0..lines.len() / 3 {
        let mut group: Vec<String> = vec![lines.pop().expect("out of bounds")];
        // TODO: find a way to pop multiple
        group.push(lines.pop().expect("out of bounds"));
        group.push(lines.pop().expect("out of bounds"));
        elf_groups.push(group);
    }

    // Find the common item in each group.
    for g in elf_groups {
        let parts: Vec<&str> = g.iter().map(|v| v as &str).collect();
        let result_substrings = get_substrings(parts, 3, 1);
        let item: char = result_substrings[0].name.chars().next().clone().unwrap();
        common_items.push(item);
    }

    // Calculate the result by adding corresponding indexes.
    for item in common_items {
        let priority: u32 = priorities.iter().position(|&x| x == item).unwrap() as u32;
        result += priority + 1;
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

    // vJrwpWtwJgWrhcsFMMfFFhFp
    // jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    // PmmdzqPrVvPwwTWBwg
    // wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    // ttgJtRGJQctTZtZT
    // CrZsJsPPZsGzwwsLwLmpwMDw

    #[test]
    fn part1_works() {
        let input = "./sample.txt";
        let result = process_part1(input);
        assert_eq!(result, "157");
    }

    #[test]
    fn part2_works() {
        let input = "./sample.txt";
        let result = process_part2(input);
        assert_eq!(result, "70");
    }
}
