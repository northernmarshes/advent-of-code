use regex::Regex;
use std::fs::read_to_string;

#[derive(Debug)]
pub struct Game {
    pub number: u32,
    pub blue: u32,
    pub green: u32,
    pub red: u32,
}

pub fn process_part1(input: &str) -> String {
    let result = 0;
    let games = read_lines(input);
    let _searched_game = Game {
        number: 0,
        blue: 6,
        green: 2,
        red: 1,
    };

    for game in games {
        let game = parse_game(&game);
        println!("The game is {game:?}");
    }
    result.to_string()
}

pub fn parse_game(hay: &str) -> Game {
    let mut game = Game {
        number: 0,
        blue: 0,
        green: 0,
        red: 0,
    };

    // regexes

    let re_blue = Regex::new(r"(\d+) blue").unwrap();
    let re_green = Regex::new(r"(\d+) green").unwrap();
    let re_red = Regex::new(r"(\d+) red").unwrap();
    let re_default = Regex::new(r"(\d+)").unwrap();
    let re_index = Regex::new(r"Game (\d+)").unwrap();

    let n = re_index.find(hay).unwrap().as_str();
    let n = n.chars().last().unwrap() as u32 - 48;
    game.number = n;

    let parts = hay.split(";");
    for part in parts {
        let b_str = re_blue
            .captures(part)
            .unwrap_or(re_default.captures("0").unwrap());
        let b_str = b_str.get(0).unwrap().as_str();
        let b = b_str
            .to_string()
            .split_whitespace()
            .next()
            .unwrap_or("0")
            .parse::<u32>()
            .unwrap_or(0);

        let g_str = re_green
            .captures(part)
            .unwrap_or(re_default.captures("0").unwrap());
        let g_str = g_str.get(0).unwrap().as_str();
        let g = g_str
            .to_string()
            .split_whitespace()
            .next()
            .unwrap_or("0")
            .parse::<u32>()
            .unwrap_or(0);

        let r_str = re_red
            .captures(part)
            .unwrap_or(re_default.captures("0").unwrap());
        let r_str = r_str.get(0).unwrap().as_str();
        let r = r_str
            .to_string()
            .split_whitespace()
            .next()
            .unwrap_or("0")
            .parse::<u32>()
            .unwrap_or(0);

        if game.blue < b {
            game.blue = b;
        }

        if game.green < g {
            game.green = g;
        }

        if game.red < r {
            game.red = r;
        }
    }

    game
}

// pub fn process_part2(input: &str) -> String {
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

    // Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    // Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    // Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    // Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    // Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

    #[test]
    fn part1_works() {
        let input = "./sample.txt";
        let result = process_part1(input);
        assert_eq!(result, "21");
    }

    // #[test]
    // fn part2_works() {
    //     let input = "./sample.txt";
    //     let result = process_part2(input);
    //     assert_eq!(result, "");
    // }
}
