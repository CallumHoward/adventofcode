// 03/part2/main.rs
// http://adventofcode.com/2017/day/3
// Callum Howard, 2017

use std::io::stdin;
use std::collections::HashMap;

type Point = (i32, i32);

fn go(point: Point, direction: Point) -> Point {
    (point.0 + direction.0, point.1 + direction.1)
}

fn adjacent(point: Point, all_directions: &Vec<Point>) -> Vec<Point> {
    all_directions.iter().map(|&direction| go(point, direction)).collect()
}

fn solve(target: i32) -> i32 {
    // directions
    let n = (0, -1);
    let nw = (-1, -1);
    let s = (0, 1);
    let se = (1, 1);
    let e = (1, 0);
    let ne = (1, -1);
    let w = (-1, 0);
    let sw = (-1, 1);
    let all_directions = vec![n, nw, s, se, e, ne, w, sw];

    let value = 1;
    let mut sroot = 1;
    let mut point = (0, 0);
    let mut values = HashMap::new();
    values.insert(point, value);

    if value > target {
        return value;
    }

    loop {
        let spiral = [
            (e, 1),
            (n, sroot),
            (w, sroot + 1),
            (s, sroot + 1),
            (e, sroot + 1),
        ];

        for &(direction, distance) in spiral.iter() {

            for _ in 0..distance {
                point = go(point, direction);

                let value = adjacent(point, &all_directions).iter()
                    .filter_map(|adjacent_point| values.get(adjacent_point))
                    .sum();
                values.insert(point, value);

                if value > target {
                    return value;
                }
            }
        }

        sroot += 2;
    }

}

fn main() {
    let mut input = String::new();

    stdin().read_line(&mut input)
        .expect("failed to read line");

    let input: i32 = input.trim().parse()
        .expect("Please type a number!");

    println!("{}", solve(input));
}
