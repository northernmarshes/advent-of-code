use std::fs::read_to_string;

pub fn process_part1(input: &str) -> String {
    let mut result: u32 = 0;
    let mut forest = make_matrix(input);
    let mut rotation = 0;
    let forest_edge = (forest.len() * 4) - 4;
    let brink = forest.len() - 1;
    result += forest_edge as u32;
    let mut seen_indexes = forest.clone();

    while rotation < 4 {
        let forest_copy = forest.clone();
        for (r, row) in forest_copy[1..brink].iter().enumerate() {
            for (c, tree) in row[1..brink].iter().enumerate() {
                let previous_highest = row[0..=c].iter().max().unwrap_or(&0);
                // 99 chosen arbitrary just to index seen trees
                if seen_indexes[r + 1][c + 1] == 99 {
                    // println!("Already seen: {tree}");
                } else if tree > previous_highest {
                    // println!("VISIBLE: {tree}");
                    let (row_index, column_index) = (r + 1, c + 1);
                    seen_indexes[row_index][column_index] = 99;
                    result += 1;
                } else {
                    // println!("INVISIBLE: {tree}");
                }
            }
            // println!(">>> NEXT LINE");
        }
        forest = rotate_matrix(forest);
        seen_indexes = rotate_matrix(seen_indexes);
        // println!("FLIP!");
        rotation += 1;
    }

    result.to_string()
}

pub fn process_part2(input: &str) -> String {
    let result: u32 = 0;
    let forest = make_matrix(input);
    let mut rotation: i32 = 0;
    let brink = forest.len() - 1;

    while rotation < 4 {
        let forest_copy = forest.clone();
        for (r, row) in forest_copy[1..brink].iter().enumerate() {
            for (c, tree) in row[1..brink].iter().enumerate() {
                // TODO:: scenic score logic
                println!("tree: {tree}")
            }
        }
        rotation += 1;
    }

    result.to_string()
}

pub fn make_matrix(input: &str) -> Vec<Vec<i8>> {
    let lines = read_lines(input);
    let mut forest_matrix: Vec<Vec<i8>> = Vec::new();
    for line in lines {
        let mut tree_row: Vec<i8> = Vec::new();
        for c in line.chars() {
            let tree = c.to_string().parse::<i8>().unwrap();
            tree_row.push(tree);
        }
        forest_matrix.push(tree_row);
    }
    forest_matrix
}

/// reverse forest matrix
pub fn rotate_matrix(input: Vec<Vec<i8>>) -> Vec<Vec<i8>> {
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

    #[test]
    fn part2_works() {
        let input = "./sample.txt";
        let result = process_part2(input);
        assert_eq!(result, "8");
    }
}
