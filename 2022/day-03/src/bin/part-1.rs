use day_03::process_part1;

fn main() {
    let file = "./input.txt";
    // let file = "./sample.txt";
    println!(
        "{} is the sum of the priorities of those item types.",
        process_part1(file)
    );
}
