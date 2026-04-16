use std::{collections::HashMap, fs::read_to_string};

pub fn process_part1(input: &str) -> String {
    let mut result: u32 = 0;
    let lines = read_lines(input);
    let mut current_folder: char = '/';
    let mut previous_folders: Vec<char> = Vec::new();
    let mut folder_sizes: HashMap<char, u32> = HashMap::new();

    // make a list of directories
    for line in &lines {
        if line.contains("dir") {
            let dir = line.clone().chars().last().unwrap();
            folder_sizes.insert(dir, 0);
        }
    }

    // main logic
    for line in lines {
        let current_line = line;
        let first_char = current_line.chars().next().unwrap();
        if current_line.contains("$") {
            if current_line.contains("cd") {
                let current_command = &current_line;
                let current_command_last = current_command.chars().last().unwrap();
                if current_command_last.is_alphanumeric() {
                    previous_folders.push(current_folder);
                    current_folder = current_command_last;
                    // println!("current folder is: {current_folder}");
                } else if current_command_last == '.' {
                    let previous = previous_folders.pop().unwrap_or('/');
                    // println!("Im going back from {current_folder} to {previous}");
                    current_folder = previous;
                } else if current_line.contains("ls") {
                    // println!("ls command triggered");
                }
            }
        } else if current_line.contains("dir") {
            // println!("directory!")
        } else if first_char.is_numeric() {
            let mut words = current_line.as_str().split_whitespace();
            let first_word = words.next().unwrap();
            let file_size = first_word.parse::<u32>().unwrap();
            let current_size = folder_sizes.get(&current_folder).copied().unwrap_or(0);
            let input = current_size + file_size;
            folder_sizes.insert(current_folder, input);
            println!(
                "its numeric and current folder is: {current_folder} and I'm inputing {file_size} and the total is {input}"
            );

            // add size to the previous folder
            //TODO: fix path tracking
            if current_folder != '/' {
                for folder in &previous_folders {
                    // let path_len = previous_folders.len();
                    // println!("path is now {path_len} long.");
                    let previous_folder = folder.clone();
                    let previous_folder_current_size =
                        folder_sizes.get(&previous_folder).copied().unwrap_or(0);
                    let previous_folder_input = previous_folder_current_size + file_size;
                    folder_sizes.insert(previous_folder, previous_folder_input);
                }
            }
        }
    }

    println!("{folder_sizes:#?}");

    // calculate sum of folders lesser then 100000
    for (_key, value) in folder_sizes {
        if value < 100000 {
            result += value;
        }
    }
    result.to_string()
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

    // #[test]
    // fn part2_works() {
    //     let input = "./sample.txt";
    //     let result = process_part2(input);
    //     assert_eq!(result, "95437");
    // }
}
