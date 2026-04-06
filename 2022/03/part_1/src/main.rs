use std::fs::read_to_string;
use common_substrings::get_substrings;

fn main() {
    let mut result:u32 = 0;
    let filename = "input.txt";
    let lines: Vec<String> = read_lines(filename);
    let mut common_items: Vec<char> = Vec::new();
    let priorities: Vec<char> = vec!['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

    // Find the common item in both compartments.
    for line in &lines {
        let (first_half, second_half) = line.split_at(line.len()/2);
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

    println!("{result} is the sum of the priorities of those item types.");
}

/// Change text file into an iterator.
fn read_lines(name: &str) -> Vec<String> {
    read_to_string(name).unwrap()
                        .lines()
                        .map(String::from)
                        .collect()
    
}
