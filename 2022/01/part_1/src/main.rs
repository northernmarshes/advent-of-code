use std::fs::read_to_string;

fn main() {
    let filename = "input.txt";
    let lines = read_lines(filename);
    let mut calories: u32 = 0;
    let mut each_elfs_calories: Vec<u32> = vec![];

    for line in lines {
        if line != "" {
            let value: u32 = line.trim().parse().expect("");
            calories += &value;
        } else {
            each_elfs_calories.push(calories);
            calories = 0;
        }
    }

    let max = each_elfs_calories.iter().max().unwrap();
    println!(
        "The elf that is carrying the most is carrying {} calories.",
        max
    );
}

/// Change text file into an iterator.
fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}
