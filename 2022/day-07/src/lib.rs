use std::fs::read_to_string;

pub fn process_part1(input: &str) -> String {
    let result: u32 = 0;
    let lines = read_lines(input);
    println!("{lines:#?}");
    result.to_string()
}

// pub fn process_part2(input: &str) -> String {
//     let mut result: u32 = 0;
//     result.to_string()
// }

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

    // $ cd /
    // $ ls
    // dir a
    // 14848514 b.txt
    // 8504156 c.dat
    // dir d
    // $ cd a
    // $ ls
    // dir e
    // 29116 f
    // 2557 g
    // 62596 h.lst
    // $ cd e
    // $ ls
    // 584 i
    // $ cd ..
    // $ cd ..
    // $ cd d
    // $ ls
    // 4060174 j
    // 8033020 d.log
    // 5626152 d.ext
    // 7214296 k

    #[test]
    fn part1_works_01() {
        let input = "./sample.txt";
        let result = process_part1(input);
        assert_eq!(result, "95437");
    }
}
