use std::fs::read_to_string;

pub fn process_part1(input: &str) -> String {
    let result = 0;
    let lines = read_lines(input);
    let mut forest_matrix: Vec<Vec<u8>> = Vec::new();
    for line in lines {
        let mut tree_row: Vec<u8> = Vec::new();
        for c in line.chars() {
            let tree = c.to_string().parse::<u8>().unwrap();
            tree_row.push(tree);
        }
        forest_matrix.push(tree_row);
    }

    println!("{forest_matrix:?}");
    result.to_string()
}

// pub fn process_part2(input: &str) -> String {
// result.to_string()
// }

// parse the input
pub fn read_lines(name: &str) -> Vec<String> {
    read_to_string(name)
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    // 30373
    // 25512
    // 65332
    // 33549
    // 35390

    #[test]
    fn part1_works() {
        let input = "./sample.txt";
        let result = process_part1(input);
        assert_eq!(result, "21");
    }

    // #[test]
    // fn part2_works() {
    //     let input = "./sample.txt";
    //     let result = process_part2(input);
    //     assert_eq!(result, "");
    // }
}
