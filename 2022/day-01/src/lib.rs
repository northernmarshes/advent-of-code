use std::fs::read_to_string;

pub fn process_part1(input: &str) -> String {
    let lines = read_lines(input);
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
    max.to_string()
}

pub fn process_part2(input: &str) -> String {
    let mut lines = read_lines(input);

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

    top_three_elves_calories.to_string()
}

/// Change text file into an iterator.
pub fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    // 1000
    // 2000
    // 3000
    //
    // 4000
    //
    // 5000
    // 6000
    //
    // 7000
    // 8000
    // 9000
    //
    // 10000

    #[test]
    fn part1_works() {
        let input = "./sample.txt";
        let result = process_part1(input);
        assert_eq!(result, "24000");
    }

    #[test]
    fn part2_works() {
        let input = "./sample.txt";
        let result = process_part2(input);
        assert_eq!(result, "45000");
    }
}
