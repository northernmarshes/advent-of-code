use day_07::process_part1;

fn main() {
    let file = "./input.txt";
    // let file = "./sample.txt";
    let result: String = process_part1(file);
    println!("{result} is the sum of the total sizes of directories smaller then 100000.");
}
