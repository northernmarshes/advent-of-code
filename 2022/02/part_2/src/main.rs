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
    for round in &rounds {
        // X - loose   0
        // Y - draw    1
        // Z - win     3

        // A  Rock     1
        // B  Paper    2
        // C  Scissors 3

        // Rock
        if round[0] == "A" && round[1] == "Y" {
            // rock
            score += 1;
            // draw
            score += 3;
        } else if round[0] == "A" && round[1] == "X" {
            // scissors
            score += 3;
            // lose
        } else if round[0] == "A" && round[1] == "Z" {
            // paper
            score += 2;
            // win
            score += 6;

            // Paper
        } else if round[0] == "B" && round[1] == "Y" {
            // paper
            score += 2;
            // draw
            score += 3;
        } else if round[0] == "B" && round[1] == "X" {
            score += 1;
            // loose
        } else if round[0] == "B" && round[1] == "Z" {
            // scissors
            score += 3;
            // win
            score += 6;

            // Scissors
        } else if round[0] == "C" && round[1] == "Y" {
            // scissors
            score += 3;
            // draw
            score += 3;
        } else if round[0] == "C" && round[1] == "X" {
            // paper
            score += 2;
            // loose
        } else if round[0] == "C" && round[1] == "Z" {
            // rock
            score += 1;
            // win
            score += 6;
        }
    }

    println!("The total score would be {score}.");
}

/// Change text file into an iterator.
fn read_lines(name: &str) -> Vec<String> {
    read_to_string(name)
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}
