use std::fs::read_to_string;

pub fn process_part1(input: &str) -> String {
    let result = 0;
    // 1. Check if char is a number
    // 2. If so mark the index
    // 3. Check any next char if its a number
    // 4. Check if there is char other then '.' and numeric surrounding
    // 5. If so mark the number as a part
    // 6. Add number to result
    let lines = read_lines(input);
    for (y_index, line) in lines.iter().enumerate() {
        for (x_index, char) in line.chars().enumerate() {
            if char.is_numeric() {
                check_part_number(x_index, y_index, &lines);
                println!(
                    "The char is {}, and it's index is {} and {}",
                    char, y_index, x_index
                );
            }
        }
    }
    result.to_string()
}

fn check_part_number(x_index: usize, y_index: usize, schematic: &Vec<String>) {
    // let mut is_part: bool = false;
    for char in schematic[y_index].chars() {
        println!("{}", char)
    }
}

pub fn process_part2(input: &str) -> String {
    let result = 0;
    result.to_string()
}

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

    // 467..114..
    // ...*......
    // ..35..633.
    // ......#...
    // 617*......
    // .....+.58.
    // ..592.....
    // ......755.
    // ...$.*....
    // .664.598..

    #[test]
    fn part1_works() {
        let input = "./sample.txt";
        let result = process_part1(input);
        assert_eq!(result, "0");
    }

    #[test]
    fn part2_works() {
        let input = "./sample.txt";
        let result = process_part2(input);
        assert_eq!(result, "0");
    }
}
