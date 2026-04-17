use rand::prelude::*;
use std::{collections::HashMap, fs::read_to_string};

pub fn process_part1(input: &str) -> String {
    let folder_sizes = read_folder_sizes(input);
    let mut result: u32 = 0;

    // calculate sum of folders lesser then 100000
    for (_key, value) in folder_sizes {
        if value < 100000 {
            result += value;
        }
    }
    result.to_string()
}

pub fn process_part2(input: &str) -> String {
    let folder_sizes = read_folder_sizes(input);
    let total_size: u32 = folder_sizes.get("/").copied().unwrap_or(0);
    let needed_space = 30000000;
    let available_space = 70000000 - total_size;
    let space_to_free = needed_space - available_space;
    let mut delete_candidates: Vec<u32> = Vec::new();

    // calculate the smallest directory to delete
    for (key, size) in &folder_sizes {
        if size > &space_to_free {
            let candidate = folder_sizes.get(key).unwrap();
            //TODO: fix the clone problem
            delete_candidates.push(candidate.clone());
        }
    }

    let folder_to_delete = delete_candidates.iter().min().unwrap();
    let result: u32 = *folder_to_delete;

    result.to_string()
}

pub fn read_folder_sizes(input: &str) -> HashMap<String, u32> {
    let lines = read_lines(input);
    let mut current_folder: String = String::from("/");
    let mut previous_folders: Vec<String> = Vec::new();
    let mut folder_sizes: HashMap<String, u32> = HashMap::new();
    let mut lines_df: Vec<String> = Vec::new();

    // adding randint to repeated folder names
    let mut rng = rand::rng();
    for line in &lines {
        if line.contains("..") {
            lines_df.push(line.clone());
        } else if line.contains("$ cd") && lines_df.contains(line) {
            let n = line.clone();
            let random: u32 = rng.random();
            let w: String = random.to_string();
            lines_df.push(n + &w);
        } else {
            lines_df.push(line.clone());
        }
    }

    // make a list of directories
    for line in &lines_df {
        if line.contains("dir") {
            let words = line.as_str().split_whitespace();
            let dir = String::from(words.last().unwrap());
            folder_sizes.insert(dir, 0);
        }
    }

    // main logic
    for line in lines_df {
        let current_line = line;
        let first_char = current_line.chars().next().unwrap();
        if current_line.contains("$") {
            if current_line.contains("cd") {
                let current_command = &current_line;
                let current_command_last = current_command.chars().last().unwrap();
                if current_command_last.is_alphanumeric() {
                    previous_folders.push(current_folder);
                    let words = current_line.as_str().split_whitespace();
                    let folder_name = words.last().unwrap();
                    current_folder = String::from(folder_name);
                } else if current_command_last == '.' {
                    let previous = previous_folders.pop().unwrap_or(String::from("/"));
                    current_folder = previous;
                } else if current_line.contains("ls") {
                }
            }
        } else if current_line.contains("dir") {
        } else if first_char.is_numeric() {
            let mut words = current_line.as_str().split_whitespace();
            let first_word = words.next().unwrap();
            let file_size = first_word.parse::<u32>().unwrap();
            let current_size = folder_sizes.get(&current_folder).copied().unwrap_or(0);
            let input = current_size + file_size;
            let key = current_folder.to_owned();
            folder_sizes.insert(key, input);

            if current_folder != "/" {
                for folder in previous_folders.iter().rev() {
                    let previous_folder = folder.clone();
                    let previous_folder_current_size =
                        folder_sizes.get(&previous_folder).copied().unwrap_or(0);
                    let previous_folder_input = previous_folder_current_size + file_size;
                    folder_sizes.insert(previous_folder, previous_folder_input);
                }
            }
        }
    }
    folder_sizes
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

    // $ cd /
    // $ ls
    // dir a
    // 14848514 b.txt
    // 8504156 c.dat
    // dir d
    // $ cd a
    // $ ls
    // dir e
    // 29116 f
    // 2557 g
    // 62596 h.lst
    // $ cd e
    // $ ls
    // 584 i
    // $ cd ..
    // $ cd ..
    // $ cd d
    // $ ls
    // 4060174 j
    // 8033020 d.log
    // 5626152 d.ext
    // 7214296 k

    #[test]
    fn part1_works() {
        let input = "./sample.txt";
        let result = process_part1(input);
        assert_eq!(result, "95437");
    }

    #[test]
    fn part2_works() {
        let input = "./sample.txt";
        let result = process_part2(input);
        assert_eq!(result, "24933642");
    }
}
