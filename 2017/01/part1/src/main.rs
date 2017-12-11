// 01/part1/main.rs
// http://adventofcode.com/2017/day/1
// Callum Howard, 2017

fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("read error");

    const RADIX: u32 = 10;
    let v: Vec<u32> = input.chars()
        .filter_map(|c| c.to_digit(RADIX)).collect();

    println!("{}", sum_if_repeated(v, 1));
    //println!("{}", sum_if_repeated(v, v.len() / 2));
}

fn sum_if_repeated(v: Vec<u32>, shift: usize) -> u32 {
    let mut sum = 0;
    for i in 0..v.len() {
        if v[i] == v[(i + shift) % v.len()] {
            sum += v[i];
        }
    }
    sum
}

fn sum_if_repeated2(v: Vec<u32>, shift: usize) -> u32 {
    (0..v.len())
        .filter(|&i| v[i] == v[(i + shift) % v.len()])
        .map(|i| v[i])
        .sum()
}

fn sum_if_repeated3(v: Vec<u32>, shift: usize) -> u32 {
    v.iter()
        .zip(v[shift..].iter().chain(v[..shift].iter()))
        .filter(|&(a, b)| a == b)
        .map(|(a, _)| a)
        .sum()
}

fn sum_if_repeated4(v: Vec<u32>, shift: usize) -> u32 {
    v.iter()
        .zip(v.iter().cycle().skip(shift))
        .filter(|&(a, b)| a == b)
        .map(|(a, _)| a)
        .sum()
}
