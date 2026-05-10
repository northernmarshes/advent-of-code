use regex::Regex;
use std::fs::read_to_string;

#[derive(Debug)]
pub struct Game {
    pub n: u32,
    pub r: u32,
    pub g: u32,
    pub b: u32,
}

pub fn process_part1(input: &str) -> String {
    let mut result = 0;
    let games = read_lines(input);
    let searched = Game {
        n: 0,
        r: 12,
        g: 13,
        b: 14,
    };

    for game in games {
        let game = parse_game(&game);
        if game.r < searched.r && game.g < searched.g && game.b < searched.b {
            let ind = game.n;
            result += ind;
            // println!("{ind}");
        }
        println!("The game is {game:?}");
    }
    result.to_string()
}

pub fn parse_game(hay: &str) -> Game {
    let mut game = Game {
        n: 0,
        b: 0,
        g: 0,
        r: 0,
    };

    let re_i = Regex::new(r"Game (\d+)").unwrap();
    let re_r = Regex::new(r"(\d+) red").unwrap();
    let re_g = Regex::new(r"(\d+) green").unwrap();
    let re_b = Regex::new(r"(\d+) blue").unwrap();
    let re_d = Regex::new(r"(\d+)").unwrap();

    let n = re_i.find(hay).unwrap().as_str();
    let n = n.split_whitespace().last().unwrap();
    let n = n.parse::<u32>().unwrap_or(0);
    game.n = n;

    let parts = hay.split(";");
    for part in parts {
        let r = count_cubes(&re_r, &re_d, part);
        let g = count_cubes(&re_g, &re_d, part);
        let b = count_cubes(&re_b, &re_d, part);

        if game.r < r {
            game.r = r;
        }
        if game.g < g {
            game.g = g;
        }
        if game.b < b {
            game.b = b;
        }
    }
    game
}

fn count_cubes(r: &Regex, rd: &Regex, h: &str) -> u32 {
    let cubes = r.captures(h).unwrap_or(rd.captures("0").unwrap());
    let cubes = cubes.get(0).unwrap().as_str();
    let d: u32 = cubes
        .to_string()
        .split_whitespace()
        .next()
        .unwrap_or("0")
        .parse::<u32>()
        .unwrap_or(0);
    d
}

// pub fn process_part2(input: &str) -> String {
//     result.to_string()
// }

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

    // Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    // Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    // Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    // Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    // Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

    #[test]
    fn part1_works() {
        let input = "./sample.txt";
        let result = process_part1(input);
        assert_eq!(result, "8");
    }

    // #[test]
    // fn part2_works() {
    //     let input = "./sample.txt";
    //     let result = process_part2(input);
    //     assert_eq!(result, "");
    // }
}
