use day_04::process_part1;

fn main() {
    let file = "./input.txt";
    // let file = "./sample.txt";
    println!(
        "In {} assignment pairs one range fully contains the other.",
        process_part1(file)
    );
}
