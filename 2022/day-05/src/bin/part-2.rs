use day_05::process_part2;

fn main() {
    let file = "./input.txt";
    // let file = "./sample.txt";
    println!(
        "{} crates end up on top of each stack.",
        process_part2(file)
    );
}
