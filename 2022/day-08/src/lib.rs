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
                // 99 chosen arbitrarily just to index seen trees
                if seen_indexes[r + 1][c + 1] == 99 {
                } else if tree > previous_highest {
                    // println!("VISIBLE: {tree}");
                    let (row_index, column_index) = (r + 1, c + 1);
                    seen_indexes[row_index][column_index] = 99;
                    result += 1;
                } else {
                    // println!("INVISIBLE: {tree}");
                }
            }
        }
        forest = rotate_matrix(forest);
        seen_indexes = rotate_matrix(seen_indexes);
        rotation += 1;
    }

    result.to_string()
}

pub fn process_part2(input: &str) -> String {
    let forest = make_matrix(input);
    let mut scores: Vec<u32> = Vec::new();

    for (r, row) in forest.iter().enumerate() {
        for (c, _column) in row.iter().enumerate() {
            let score: u32 = scenic_score(r, c, forest.clone());
            scores.push(score);
        }
    }

    let result = scores.iter().max().unwrap_or(&0);
    result.to_string()
}

pub fn scenic_score(row: usize, col: usize, vec: Vec<Vec<i8>>) -> u32 {
    let mut r = row;
    let mut c = col;
    let mut score: u32 = 1;
    let mut forest = vec;
    let tree = forest[r][c];
    let mut rot = 0;
    let rotations = 4;
    let mut seen_vec: Vec<u32> = Vec::new();

    while rot < rotations {
        let forest_copy = forest.clone();
        let edge = forest_copy.len() - 1;
        let mut seen = 0;
        for n in c..edge {
            let next = forest[r][n + 1];
            if next < tree {
                seen += 1;
            } else {
                seen += 1;
                break;
            }
        }
        // println!("From tree: {tree} I see: {seen} in iteration nr {rot}");
        seen_vec.push(seen);

        // rotate index
        let temp = r;
        r = c;
        c = forest.len() - 1 - temp;

        // rotate matrix
        forest = rotate_matrix(forest);
        rot += 1;
    }

    // mutliply scores
    for i in seen_vec {
        score *= i;
    }
    score
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

    #[test]
    fn scenic_score_works() {
        let vector: Vec<Vec<i8>> = vec![
            vec![3, 0, 3, 7, 3],
            vec![2, 5, 5, 1, 2],
            vec![6, 5, 3, 3, 2],
            vec![3, 3, 5, 4, 9],
            vec![3, 5, 3, 9, 0],
        ];
        let r: usize = 3;
        let c: usize = 2;
        let result = scenic_score(r, c, vector);
        assert_eq!(result, 8);
    }
}
