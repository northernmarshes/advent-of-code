use std::{collections::HashSet, fs::read_to_string};

#[derive(Debug)]
pub struct Cmd {
    pub dir: char,
    pub dis: u8,
}

#[derive(Debug)]
pub struct Line {
    pub h_x: i64,
    pub h_y: i64,
    pub t_x: i64,
    pub t_y: i64,
}

#[derive(Debug)]
pub struct EndPoint {
    pub x: f64,
    pub y: f64,
}

impl EndPoint {
    fn distance_to(&self, other: &EndPoint) -> f64 {
        ((self.x - other.x).powi(2) + (self.y - other.y).powi(2)).sqrt()
    }
}

pub fn process_part1(input: &str) -> String {
    let mut positions: HashSet<(u32, u32)> = HashSet::new();
    let start: (u32, u32) = (0, 0);
    positions.insert(start);
    let raw_commands = read_lines(input);
    let commands = parse_commands(raw_commands);
    let mut line = Line {
        h_x: 0,
        h_y: 0,
        t_x: 0,
        t_y: 0,
    };

    let mut l = &mut line;
    for command in commands {
        let (line_pos, tail_positions) = move_rope(l, command);
        for pos in tail_positions {
            positions.insert(pos);
        }
        l = line_pos;
        // println!("line is at: {head_position:?}");
    }

    // println!("{positions:?}");
    let result = positions.len();
    result.to_string()
}

// pub fn process_part2(input: &str) -> String {
//     let result = 0;
//     result.to_string()
// }

pub fn move_rope(line: &mut Line, command: Cmd) -> (&mut Line, HashSet<(u32, u32)>) {
    let distance = command.dis;
    let mut positions: HashSet<(u32, u32)> = HashSet::new();

    for _step in 0..distance {
        match command.dir {
            'U' => line.h_y += 1,
            'D' => line.h_y -= 1,
            'R' => line.h_x += 1,
            'L' => line.h_x -= 1,
            _ => println!("This ain't a direction!"),
        };

        let head = EndPoint {
            x: line.h_x as f64,
            y: line.h_y as f64,
        };

        let tail = EndPoint {
            x: line.t_x as f64,
            y: line.t_y as f64,
        };

        let head_tail_distance = head.distance_to(&tail);

        if head_tail_distance >= 2.0 {
            if command.dir == 'U' {
                line.t_x = line.h_x;
                line.t_y = line.h_y - 1;
            } else if command.dir == 'D' {
                line.t_x = line.h_x;
                line.t_y = line.h_y + 1;
            } else if command.dir == 'R' {
                line.t_x = line.h_x - 1;
                line.t_y = line.h_y;
            } else {
                line.t_x = line.h_x + 1;
                line.t_y = line.h_y;
            }

            let position = (line.t_x as u32, line.h_y as u32);
            positions.insert(position);

            // println!("The distance is: {head_tail_distance}. and the positions are {line:?}");
        }
    }
    (line, positions)
}

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
