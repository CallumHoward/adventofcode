// 03/part1/main.rs
// http://adventofcode.com/2017/day/3
// Callum Howard, 2017

use std::io::stdin;

type Point = (i32, i32);

// directions
const N: Point = (0, -1);
const S: Point = (0, 1);
const E: Point = (1, 0);
const W: Point = (-1, 0);

fn spiral(square_root: i32) -> [(Point, i32); 5] {
    [
        (E, 1),
        (N, square_root),
        (W, square_root + 1),
        (S, square_root + 1),
        (E, square_root + 1),
    ]
}

fn go(point: Point, direction: Point) -> Point {
    (point.0 + direction.0, point.1 + direction.1)
}

fn prev_odd_square(input: i32) -> i32 {
    let n = (input as f32).sqrt() as i32;
    if is_even(n) { n - 1 } else { n }
}

fn find_diagonal(square: i32) -> (i32, i32) {
    (square / 2, square / 2)
}

fn manhattan(point: Point) -> i32 {
    point.0.abs() + point.1.abs()
}

fn is_even(n: i32) -> bool {
    n % 2 == 0
}

fn solve(target: i32) -> i32 {
    let square_root = prev_odd_square(target);
    let mut point = find_diagonal(square_root);
    let mut index = square_root * square_root;

    for &(direction, distance) in spiral(square_root).iter() {
        for _ in 0..distance {
            point = go(point, direction);
            index += 1;

            if index == target {
                return manhattan(point);
            }
        }
    }

    0
}

fn main() {
    let mut input = String::new();

    stdin().read_line(&mut input)
        .expect("failed to read line");

    let input: i32 = input.trim().parse()
        .expect("Please type a number!");

    println!("{}", solve(input));
}
