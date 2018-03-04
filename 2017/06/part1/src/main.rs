// part1.rs
// http://adventofcode.com/2017/day/6

use std::io::stdin;
use std::collections::HashSet;

fn main() {
    //assert!(redistribute((0, 2, 7, 0)) == (2, 4, 1, 2));
    //assert!(solve((0, 2, 7, 0)) == 5);

    let mut input = String::new();

    stdin().read_line(&mut input)
        .expect("failed to read line");

    let input = &mut input.split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    println!("{}", solve(input));
}

fn solve(input: &mut Vec<i32>) -> i32 {
    let mut banks = HashSet::new();

    for reallocations in 0.. {
       if !banks.insert(input.clone()) {
          return reallocations;
       }

       redistribute(input);
    }

    0
}

fn max_index(sequence: Vec<i32>) -> (usize, i32) {
    let mut max_index : usize = 0;
    let mut max_element = 0;

    for (i, e) in sequence.iter().enumerate() {
        if e > &max_element {
            max_index = i;
            max_element = *e;
        }
    }

    (max_index, max_element)
}

fn redistribute(input: &mut Vec<i32>) {
    let (index, element) = max_index(input.to_vec());
    input[index] = 0;

    for offset in 1..element + 1 {
        let size = input.len();
        input[(index + offset as usize) % size] += 1;
    }
}
