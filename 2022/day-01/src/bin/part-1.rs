use day_01::process_part1;

fn main() {
    let file = "./input.txt";
    // let file = "./sample.txt";
    println!(
        "The elf that is carrying the most is carrying {} calories.",
        process_part1(file)
    );
}
