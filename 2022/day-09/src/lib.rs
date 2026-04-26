use std::{collections::HashSet, fs::read_to_string};

#[derive(Debug)]
pub struct Cmd {
    pub dir: char,
    pub dis: u8,
}

#[derive(Debug)]
pub struct ShortLine {
    pub h_x: i64,
    pub h_y: i64,
    pub t_x: i64,
    pub t_y: i64,
}

#[derive(Debug)]
pub struct LinePoint {
    pub x: i64,
    pub y: i64,
}

#[derive(Debug)]
pub struct LongLine {
    pub head: LinePoint,
    pub p_9: LinePoint,
    pub p_8: LinePoint,
    pub p_7: LinePoint,
    pub p_6: LinePoint,
    pub p_5: LinePoint,
    pub p_4: LinePoint,
    pub p_3: LinePoint,
    pub p_2: LinePoint,
    pub tail: LinePoint,
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
    let mut positions: HashSet<(i64, i64)> = HashSet::new();
    let start: (i64, i64) = (0, 0);
    positions.insert(start);
    let raw_commands = read_lines(input);
    let commands = parse_commands(raw_commands);
    let mut line = ShortLine {
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
    }

    let result = positions.len();
    result.to_string()
}

pub fn process_part2(input: &str) -> String {
    let result = 0;
    let mut positions: HashSet<(i64, i64)> = HashSet::new();
    let start: (i64, i64) = (0, 0);
    positions.insert(start);
    let raw_commands = read_lines(input);
    let _commands = parse_commands(raw_commands);
    let mut line = LongLine {
        head: LinePoint { x: 0, y: 0 },
        p_9: LinePoint { x: 0, y: 0 },
        p_8: LinePoint { x: 0, y: 0 },
        p_7: LinePoint { x: 0, y: 0 },
        p_6: LinePoint { x: 0, y: 0 },
        p_5: LinePoint { x: 0, y: 0 },
        p_4: LinePoint { x: 0, y: 0 },
        p_3: LinePoint { x: 0, y: 0 },
        p_2: LinePoint { x: 0, y: 0 },
        tail: LinePoint { x: 0, y: 0 },
    };

    result.to_string()
}

pub fn move_rope(line: &mut ShortLine, command: Cmd) -> (&mut ShortLine, HashSet<(i64, i64)>) {
    let distance = command.dis;
    let mut positions: HashSet<(i64, i64)> = HashSet::new();

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

            let position = (line.t_x, line.t_y);
            positions.insert(position);
        }
    }
    (line, positions)
}

pub fn move_long_rope(line: &mut LongLine, _command: Cmd) -> (&mut LongLine, HashSet<(i64, i64)>) {
    let positions: HashSet<(i64, i64)> = HashSet::new();
    // TODO: write long line logic
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

    #[test]
    fn part2_works() {
        let input = "./sample.txt";
        let result = process_part2(input);
        assert_eq!(result, "1");
    }

    // R 5
    // U 8
    // L 8
    // D 3
    // R 17
    // D 10
    // L 25
    // U 20

    #[test]
    fn part2_works_large() {
        let input = "./sample_large.txt";
        let result = process_part2(input);
        assert_eq!(result, "36");
    }
}
