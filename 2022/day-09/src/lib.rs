use std::fs::read_to_string;

#[derive(Debug)]
pub struct Cmd {
    pub dir: char,
    pub dis: u8,
}

pub fn process_part1(input: &str) -> String {
    let result = 0;
    // let mut height = 0;
    // let mut width = 0;
    let raw_commands = read_lines(input);
    let mut bridge: Vec<Vec<char>> = vec![vec!['O'; 15], vec!['O'; 15]];
    let mut _positions_map = bridge.clone();
    let commands = parse_commands(raw_commands);
    bridge[0][0] = 'H';

    println!("{commands:?}");

    result.to_string()
}

// pub fn process_part2(input: &str) -> String {
//     let result = 0;
//     result.to_string()
// }

pub fn parse_commands(cmd: Vec<String>) -> Vec<Cmd> {
    let mut commands: Vec<Cmd> = Vec::new();
    for line in cmd {
        let c = line
            .split_ascii_whitespace()
            .next()
            .unwrap()
            .chars()
            .next()
            .expect("Not found");
        let d = line
            .split_ascii_whitespace()
            .last()
            .unwrap()
            .parse::<u8>()
            .unwrap();
        let cmd = Cmd { dir: c, dis: d };
        commands.push(cmd);
    }
    commands
}

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

    // R 4
    // U 4
    // L 3
    // D 1
    // R 4
    // D 1
    // L 5
    // R 2

    #[test]
    fn part1_works() {
        let input = "./sample.txt";
        let result = process_part1(input);
        assert_eq!(result, "13");
    }

    // #[test]
    // fn part2_works() {
    //     let input = "./sample.txt";
    //     let result = process_part2(input);
    //     assert_eq!(result, "");
    // }
}
