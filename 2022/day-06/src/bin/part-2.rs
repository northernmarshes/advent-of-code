use day_06::process_part2;

fn main() {
    let file = "./input.txt";
    // let file = "./sample_1.txt";
    println!(
        "{} characters need to be processed before the first start-of-message marker is detected.",
        process_part2(file)
    );
}
