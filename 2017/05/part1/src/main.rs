// part1.rs
// http://adventofcode.com/2017/day/5

use std::io::{stdin, BufRead};

fn main() {
    let in_stream = stdin();

    //assert(solve([0, 3, 0, 1, -3], 0) == 10);
    //assert(solve([1, 3, 0, 1, -3], 0) == 9);
    //assert(solve([2, 3, 0, 1, -3], 1) == 8);
    //assert(solve([2, 2, 0, 1, -3], 4) == 7);

    let numbers: Vec<i32> = in_stream.lock()
        .lines()
        .filter_map(|x| x.ok())
        .map(|s| s.parse().unwrap())
        .collect();

    print!("{:?}\n", solve(numbers));
}

fn solve(mut numbers: Vec<i32>) -> i32 {
    let mut index: i32 = 0;

    for step in 1.. {
        let temp = numbers[index as usize];

        if temp < 3 {
           numbers[index as usize] += 1;
       } else {
           numbers[index as usize] -= 1;
       }

        index += temp;
        if !(0 <= index && (index as usize) < numbers.len()) {
            return step;
        }
    }

    0
}
