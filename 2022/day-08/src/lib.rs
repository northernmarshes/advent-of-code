use std::fs::read_to_string;

pub fn process_part1(input: &str) -> String {
    let mut result: u32 = 0;
    let _trees_seen: u32 = 0;
    let forest = make_matrix(input);
    let forest_edge = (forest.len() * 2) + (forest[0].len() * 2) - 4;
    let mut rotation = 4;
    let brink = forest.len() - 1;
    result += forest_edge as u32;
    // println!("{forest:?}");

    while rotation > 0 {
        for row in forest[1..brink].iter() {
            for (i, tree) in row[1..brink].iter().enumerate() {
                let previous_highest = row[0..=i].iter().max().unwrap_or(&0);
                if tree > previous_highest {
                    result += 1;
                }
            }
            println!("next line");
        }
        rotation -= 1;
    }

    result.to_string()
}

// pub fn process_part2(input: &str) -> String {
// result.to_string()
// }

pub fn make_matrix(input: &str) -> Vec<Vec<u8>> {
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
    forest_matrix
}

/// reverse forest matrix
pub fn rotate_matrix(input: Vec<Vec<u8>>) -> Vec<Vec<u8>> {
    let mut matrix = input.clone();
    for i in 0..matrix.len() {
        for j in i + 1..matrix.len() {
            let temp = matrix[j][i];
            matrix[j][i] = matrix[i][j];
            matrix[i][j] = temp;
        }
    }
    for row in &mut matrix {
        row.reverse();
    }

    matrix
}

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
