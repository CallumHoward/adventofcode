extern crate itertools;

use itertools::Itertools;
use std::io::{stdin, BufRead};

fn main() {
    let mut sum = 0;
    let in_stream = stdin();

    for line in in_stream.lock().lines() {
        let ns: Vec<u32> = line.unwrap()
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();
        let (a, b) = evenly_divisible_pair(ns.iter()).unwrap();
        sum += a / b;
    }

    println!("{}", sum);
}

// fn evenly_divisible_pair(ns: Vec<u32>) -> Option<(u32, u32)> {
fn evenly_divisible_pair<'a, I>(it: I) -> Option<(&'a u32, &'a u32)>
where
    I: Iterator<Item = &'a u32>,
{
    for ps in it.combinations(2) {
        let a = *ps.iter().max().unwrap();
        let b = *ps.iter().min().unwrap();
        if a % b == 0 {
            return Some((a, b));
        }
    }
    None
}
