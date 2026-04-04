use std::fs::read_to_string;

fn main() {
    let filename = "input.txt";
    let mut lines = read_lines(filename);

    // Add empty line to the end of the file.
    let blank_line = String::from("");
    lines.push(blank_line);

    let mut calories: u32 = 0;
    let mut top_three_elves_calories: u32 = 0;
    let mut each_elfs_calories: Vec<u32> = vec![];
    
    // Calculate calories of each elf.
    for line in lines {
        if line != "" {
        let value: u32 = line.trim().parse().expect("");
        calories += &value;
        } else {
            each_elfs_calories.push(calories);
            calories = 0;
        }
    }
    
    // Sort elves by owned calories.
    each_elfs_calories.sort();

    // Add three top three amounts.
    for n in 1..=3 {
        top_three_elves_calories += each_elfs_calories[each_elfs_calories.len() - n];
    }
    
    println!("The calories from top three elves is {}.", top_three_elves_calories);
}

/// Change text file into an iterator.
fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename).unwrap()
                            .lines()
                            .map(String::from)
                            .collect()
}
