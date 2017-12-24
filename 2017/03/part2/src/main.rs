// 03/part2/main.rs
// http://adventofcode.com/2017/day/3
// Callum Howard, 2017

use std::io::stdin;
use std::collections::HashMap;

type Point = (i32, i32);

// directions
const N: Point = (0, -1);
const NW: Point = (-1, -1);
const S: Point = (0, 1);
const SE: Point = (1, 1);
const E: Point = (1, 0);
const NE: Point = (1, -1);
const W: Point = (-1, 0);
const SW: Point = (-1, 1);
const ALL_DIRECTIONS: [Point; 8] = [N, NW, S, SE, E, NE, W, SW];

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

fn adjacent(point: Point) -> Vec<Point> {
    ALL_DIRECTIONS.iter()
        .map(|&direction| go(point, direction))
        .collect()
}

fn is_odd(n: i32) -> bool {
    n % 2 == 1
}

fn solve(target: i32) -> i32 {
    let mut point = (0, 0);
    let mut values = HashMap::new();
    values.insert(point, 1);

    for square_root in (1..).filter(|&x| is_odd(x)) {
        for &(direction, distance) in spiral(square_root).iter() {
            for _ in 0..distance {
                point = go(point, direction);

                let value = adjacent(point).iter()
                    .filter_map(|adjacent_point| values.get(adjacent_point))
                    .sum();
                values.insert(point, value);

                if value > target {
                    return value;
                }
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
