use std::fs::read_to_string;

pub struct Card {
    pub winning: Vec<u32>,
    pub given: Vec<u32>,
}

pub fn process_part1(input: &str) -> String {
    let result = 0;
    let lines: Vec<String> = read_lines(input);
    let mut deck: Vec<Card> = Vec::new();
    for line in lines {
        let card = prepare_cards(&line);
        deck.push(card);
    }
    for card in deck {
        println!("winning: {:?}, given: {:?}", card.winning, card.given);
    }
    result.to_string()
}

pub fn process_part2(_input: &str) -> String {
    let result = 0;
    result.to_string()
}

pub fn prepare_cards(card: &str) -> Card {
    let mut parts = card.split("|").clone();
    let w = parts.next().unwrap()[7..].to_string();
    let g = parts.next().unwrap().to_string();
    let mut w_numeric: Vec<u32> = Vec::new();
    let mut g_numeric: Vec<u32> = Vec::new();

    for n in w.trim().split(" ") {
        println!("linia {}", n);
        let num: u32 = n.parse().unwrap_or_default();
        w_numeric.push(num);
    }
    for n in g.trim().split(" ") {
        println!("linia {}", g);
        let num: u32 = n.parse().unwrap_or_default();
        g_numeric.push(num);
    }

    Card {
        winning: w_numeric,
        given: g_numeric,
    }
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

    // Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    // Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    // Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    // Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    // Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    // Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

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
        assert_eq!(result, "0");
    }
}
