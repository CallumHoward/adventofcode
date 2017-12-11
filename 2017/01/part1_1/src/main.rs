// 01/part1_1/main.rs
// http://adventofcode.com/2017/day/1
// Callum Howard, 2017

fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("read error");

    const RADIX: u32 = 10;
    let v: Vec<u32> = input.chars()
        .filter_map(|c| c.to_digit(RADIX)).collect();

    println!("{}", sum_if_repeated(v));
}

fn sum_if_repeated(v: Vec<u32>) -> u32 {
    let shift = v.len() / 2;
    v.iter()
        .zip(v[shift..].iter().chain(v[..shift].iter()))
        .filter(|&(a, b)| a == b)
        .map(|(a, _)| a)
        .sum()
}
