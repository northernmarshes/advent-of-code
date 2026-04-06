use std::fs::read_to_string;
use common_substrings::get_substrings;

fn main() {
    let mut result:u32 = 0;
    let filename = "input.txt";
    let mut lines: Vec<String> = read_lines(filename);
    let mut common_items: Vec<char> = Vec::new();
    let mut elf_groups: Vec<Vec<String>> = Vec::new();
    let priorities: Vec<char> = vec!['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

    // Group elves into groups of three.
    for _num in 0..lines.len() / 3 {
        let mut group:Vec<String> = Vec::new();
        // TODO: find a way to pop multiple
        group.push(lines.pop().expect("out of bounds"));
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

    println!("{result} is the sum of the priorities of those item types.");
}

/// Change text file into an iterator.
fn read_lines(name: &str) -> Vec<String> {
    read_to_string(name).unwrap()
                        .lines()
                        .map(String::from)
                        .collect()
    
}
