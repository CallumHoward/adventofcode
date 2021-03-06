// 02/part1/main.rs
// http://adventofcode.com/2017/day/2
// Callum Howard, 2017

use std::io::{stdin, BufRead};

fn main() {
    let mut sum = 0;
    let in_stream = stdin();

    for line in in_stream.lock().lines() {
        let ns: Vec<u32> = line.unwrap()
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();
        sum += ns.iter().max().unwrap() - ns.iter().min().unwrap();
    }

    println!("{}", sum);
}
