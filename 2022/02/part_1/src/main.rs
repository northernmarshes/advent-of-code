use std::fs::read_to_string;

fn main() {
    let filename = "input.txt";
    let lines = read_lines(filename);
    let mut rounds: Vec<Vec<&str>> = Vec::new();
    let mut score: u32 = 0;

    // Append rounds as a vector of vectors
    for line in &lines {
        let round = line.split(" ").collect::<Vec<&str>>();
        rounds.push(round);
    }

    // Game logic
    for round in &rounds{
        if round[0] == "A" && round[1] == "Y" {
            score += 2;
            score += 6;
        } else if round[0] == "A" && round[1] == "X" {
            score += 3;
            score += 1;
        } else if round[0] == "A" && round[1] == "Z" {
            score += 3;
        } else if round[0] == "B" && round[1] == "Y" {
            score += 3;
            score += 2;
        } else if round[0] == "B" && round[1] == "X" {
            score += 1;
        } else if round[0] == "B" && round[1] == "Z" {
            score += 6;
            score += 3;
        } else if round[0] == "C" && round[1] == "Y" {
            score += 2;
        } else if round[0] == "C" && round[1] == "X" {
            score += 6;
            score += 1;
        } else if round[0] == "C" && round[1] == "Z" {
            score += 3;
            score += 3;
        }
    }

    println!("The total score would be {score}.");
}

/// Change text file into an iterator.
fn read_lines(name: &str) -> Vec<String> {
    read_to_string(name).unwrap()
                        .lines()
                        .map(String::from)
                        .collect()
}
