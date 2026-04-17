use day_07::process_part2;

fn main() {
    let file = "./input.txt";
    // let file = "./sample.txt";
    let result = process_part2(file);
    println!(
        "{result} is the smallest directory that, if deleted, would free up enough space on the filesystem to run the update."
    );
}
