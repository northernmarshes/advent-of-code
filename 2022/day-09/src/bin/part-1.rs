use day_09::process_part1;

fn main() {
    let file = "./input.txt";
    // let file = "./sample.txt";
    let result = process_part1(file);
    println!("The tail of the rope visits {result} positions at least once.");
}
