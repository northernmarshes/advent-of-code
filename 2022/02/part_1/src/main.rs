use std::fs::read_to_string;

fn main() {
    let filename = "sample.txt";
    let lines = read_lines(filename);
    let mut rounds: Vec<(char, char)> = vec![];
    
    for line in lines {
        // let round: Vec<char, char, char> = line.chars().collect();
        println!("line: {line}");
        // println!("round: {:?}", round);
        // rounds.push(round);
    }

}

/// Change text file into an iterator.
fn read_lines(name: &str) -> Vec<String> {
    read_to_string(name).unwrap()
                        .lines()
                        .map(String::from)
                        .collect()
}
