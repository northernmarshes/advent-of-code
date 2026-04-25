use std::fs::read_to_string;

#[derive(Debug)]
pub struct Cmd {
    pub dir: char,
    pub dis: u8,
}

#[derive(Debug)]
pub struct Line {
    pub h_x: usize,
    pub h_y: usize,
    pub t_x: usize,
    pub t_y: usize,
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
    let mut result = 0;
    let raw_commands = read_lines(input);
    let commands = parse_commands(raw_commands);
    let mut line = Line {
        h_x: 0,
        h_y: 0,
        t_x: 0,
        t_y: 0,
    };

    for command in commands {
        let l = &mut line;
        let (position, m) = move_rope(l, command);
        result += m;
        println!("line is at: {position:?}");
    }

    result.to_string()
}

// pub fn process_part2(input: &str) -> String {
//     let result = 0;
//     result.to_string()
// }

pub fn move_rope(line: &mut Line, command: Cmd) -> (&Line, u32) {
    let distance = command.dis;
    let mut tail_moves = 0;

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

        let distance = head.distance_to(&tail);

        if distance > 1.0 {
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

            tail_moves += 1;
            // println!("The distance is: {distance}");
        }
    }
    (line, tail_moves)
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
