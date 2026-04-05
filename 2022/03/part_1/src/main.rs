use std::fs::read_to_string;

fn main() {
    let mut result:u32 = 0;
    let filename = "sample.txt";
    let lines: Vec<String> = read_lines(filename);
    let mut common_items: Vec<char> = Vec::new();

    for line in &lines {
        let (first_half, second_half) = line.split_at(line.len()/2);
        println!("{first_half}, {second_half}");
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
