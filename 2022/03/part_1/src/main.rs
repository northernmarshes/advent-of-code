use std::fs::read_to_string;
use common_substrings::get_substrings;

fn main() {
    let result:u32 = 0;
    let filename = "sample.txt";
    let lines: Vec<String> = read_lines(filename);
    let mut common_items: Vec<char> = Vec::new();

    for line in &lines {
        let (first_half, second_half) = line.split_at(line.len()/2);
        let mut rucksacks: Vec<&str> = vec![first_half, second_half];
        // println!("{rucksacks:?}");
        let result_substrings = get_substrings(rucksacks, 2, 1);
        // println!("{:?}, &result_substrings")
        let item: char = result_substrings[0].name.chars().next().clone().unwrap();
        // println!("{item}");
        common_items.push(item);
        
    }

    println!("{common_items:?}");

    println!("{result} is the sum of the priorities of those item types.");
}

/// Change text file into an iterator.
fn read_lines(name: &str) -> Vec<String> {
    read_to_string(name).unwrap()
                        .lines()
                        .map(String::from)
                        .collect()
    
}
