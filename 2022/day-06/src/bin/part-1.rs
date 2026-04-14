use day_06::process_part1;

fn main() {
    let file = "./input.txt";
    // let file = "./sample_1.txt";
    let result: String = process_part1(file);
    println!(
        "{result} characters need to be processed before the first start-of-packet marker is detected."
    );
}
