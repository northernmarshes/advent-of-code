use day_01::process_part2;

fn main() {
    let file = "./input.txt";
    // let file = "./sample.txt";
    println!(
        "The calories from top three elves is {}.",
        process_part2(file)
    );
}
